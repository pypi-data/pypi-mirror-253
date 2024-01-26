from kye.types import Type, TYPE_REF, EDGE
from kye.loader.loader import Loader, struct_pack
from duckdb import DuckDBPyConnection, DuckDBPyRelation
import kye.parser.kye_ast as AST

def struct_pack(edges: list[str], r: DuckDBPyRelation):
    return 'struct_pack(' + ','.join(
        f'''"{edge_name}":="{edge_name}"'''
        for edge_name in edges
            if edge_name in r.columns
    ) + ')'

def string_list(strings: list[str]):
    # TODO: Escape strings
    return "'" + "','".join(strings) + "'"

def flag(err_msg: str, condition: str, r: DuckDBPyRelation, **kwargs):
    fields = ["'" + err_msg + "'"]
    for field in ['tbl','idx','row','col','val']:
        if field in kwargs:
            if kwargs[field] is None:
                fields.append('NULL')
            else:
                fields.append("'" + kwargs[field] + "'")
        elif field in r.columns:
            fields.append(field)
        else:
            fields.append('NULL')
    
    err = r.filter(condition).select(','.join(fields))
    err.insert_into('errors')
    return r.filter(f'''NOT({condition})''')

def collect(groupby, relations: dict[str, DuckDBPyRelation]):
    collected = None
    for alias, r in relations.items():
        assert len(r.columns) == 2
        assert r.columns[0] == groupby
        r = r.select(f'''{groupby}, {r.columns[1]} as {alias}''').set_alias(alias)
        collected = collected.join(r, groupby, how='outer') if collected else r
    return collected

def row_index(r: DuckDBPyRelation, index: list[str], name: str = 'idx'):
    r = r.filter(' AND '.join(f'{idx} IS NOT NULL' for idx in index))\
        .select(f'''row, hash({struct_pack(sorted(index), r)}) as {name}''')
    return r

def row_indexes(edges: DuckDBPyRelation, typ: Type):
    global_index = row_index(edges, typ.index).set_alias('idx')
    partial_index = None
    for idx in typ.indexes:
        r = row_index(edges, idx, name='partial')
        partial_index = partial_index.union(r) if partial_index else r
    r = partial_index.join(global_index, 'row', how='left')
    # Create a map of partial ids to full ids
    partial_map = r.aggregate('partial, unnest(list_distinct(list(idx))) as idx').set_alias('partial_map')
    # Redefine index using the partial_map
    r = r.select('row, partial').join(partial_map, 'partial', how='left')
    return r

def compute_index(typ: Type, db: DuckDBPyConnection):
    table = db.table('edges').filter(f'''tbl = '{typ.ref}' ''')
    edges = table.filter(f'''col in ({string_list(typ.index)})''')
    edges = flag('MULTIPLE_INDEX_VALUES', 'cnt > 1',
        edges.aggregate('''row, col, first(val) as val, count(distinct(val)) as cnt'''), tbl=typ.ref, val=None)
    edges = collect('row', {
        col: edges.filter(f"col = '{col}'").select('row, val')
        for col in typ.index
    })
    indexes = row_indexes(edges, typ)
    r = table.aggregate('row').join(indexes, 'row', how='left')
    r = flag('MISSING_INDEX', 'partial IS NULL', r, tbl=typ.ref)
    r = flag('MISSING_INDEX_COMPLETION', 'idx IS NULL', r, tbl=typ.ref)
    r = flag('CONFLICTING_INDEX', 'cnt > 1',
        r.aggregate('row, first(idx) as idx, count(distinct(idx)) as cnt'), tbl=typ.ref, idx=None)
    print('hi')

class Table:
    typ: Type
    r: DuckDBPyRelation

    def __init__(self, typ: Type, edges: DuckDBPyRelation):
        self.typ = typ
        self.r = edges.filter(f'''tbl = '{typ.ref}' ''')
        self.flag_multiple_index_values()
        self.flag_missing_index()
        print('hi')
    
    def string_list(self, strings: list[str]):
        # TODO: Escape strings
        return "'" + "','".join(strings) + "'"

    def flag_multiple_index_values(self):
        self.flag(
            'MULTIPLE_INDEX_VALUES',
            self.r.aggregate('row, col, count(distinct val) > 1 as has_many')\
                .filter(f'''has_many AND col in ({self.string_list(self.typ.index)})''')
        )
    
    def flag_missing_index(self):
        has_one_of_the_indexes = ' OR '.join(
            f'''list_has_all(columns, [{self.string_list(idx)}])'''
            for idx in self.typ.indexes
        )
        self.flag(
            'MISSING_INDEX',
            self.r.aggregate("row, list(distinct(col)) as columns") \
                  .filter(f'NOT ({has_one_of_the_indexes})')
        )
    
    def flag(self, err, r: DuckDBPyRelation):
        err = r.select("'{err}' as err, '{tbl}' as tbl, {row_col_val}".format(
            err=err,
            tbl=self.typ.ref,
            row_col_val=','.join([
                field if field in r.columns else 'NULL'
                for field in ['row','col','val']
            ])
        ))
        err.insert_into('errors')

    def row_columns(self):
        return self.r.aggregate("row, list(distinct(col)) as columns")

    def row_defines(self, columns: list[str]):
        return self.row_columns().select(f'''row, list_has_all(columns, ['{"','".join(columns)}']) as defines''')

    def row_edge(self, edge: EDGE):
        r = self.r.filter(f"col = '{edge}'")
        return r.aggregate(f'''row, first(val) as val''')

    def collect(self, groupby, relations: dict[str, DuckDBPyRelation]):
        collected = self.r.aggregate(groupby)
        for alias, r in relations.items():
            assert len(r.columns) == 2
            assert r.columns[0] == groupby
            r = r.select(f'''{groupby}, {r.columns[1]} as {alias}''').set_alias(alias)
            collected = collected.join(r, groupby, how='left')
        return collected
    
    def row_index(self, index: list[str]):
        r = self.collect('row', {
            idx: self.row_edge(idx)
            for idx in index
        })
        r = r.select(f'''row, hash({struct_pack(sorted(index), r)}) as idx''')
        r = self.collect('row', {
            'idx': r,
            'defines': self.row_defines(index)
        }).filter('defines').select('row, idx')
        return r

    def row_indexes(self):
        global_index = self.row_index(self.typ.index).set_alias('idx')
        partial_index = None
        for idx in self.typ.indexes:
            r = self.row_index(idx).select(f"row, idx as partial")
            if partial_index is None:
                partial_index = r
            else:
                partial_index = partial_index.union(r)
        r = partial_index.join(global_index, 'row', how='left')
        partial_map = r.aggregate('partial, unnest(list_distinct(list(idx))) as idx').set_alias('partial_map')
        r = r.select('row, partial').join(partial_map, 'partial').aggregate('row, list(distinct idx) as idx')
        print('hi')
        # r = self.collect('row',{
        #     'idx': self.row_index(self.typ.index),
        #     **({
        #         f'idx_{i}': self.row_index(idx)
        #         for i,idx in enumerate(self.typ.indexes)
        #     }),
        # })
        # partial_map = r.select('idx, unnest(list_value(idx_0,idx_1)) as partial')\
        #     .filter('idx IS NOT NULL AND partial IS NOT NULL')\
        #     .aggregate('partial, list_any_value(list(idx)) as idx, count(distinct idx) as cnt')
        # return r
    
    def get_edge(self, edge: EDGE):
        assert self.typ.has_edge(edge)
        return self.r.filter("col = 'id'").select(f'row, val as {"id"}').set_alias(self.typ.ref + '.' + edge)
        if edge in self.r.columns:
            edge_rel = self.r.select(f'''_index, {edge} as val''')
        else:
            # TODO: Could probably also make this an empty table
            edge_rel = self.r.select(f'''_index, CAST(NULL as VARCHAR) as val''')

        # Create a list of each distinct value
        if edge_rel.val.dtypes[0].id == 'list':
            edge_rel = edge_rel.aggregate(f'''_index, list_distinct(flatten(list(val))) as val''')
        else:
            edge_rel = edge_rel.aggregate(f'''_index, list_distinct(list(val)) as val''')



class Validate:
    loader: Loader
    tables: dict[TYPE_REF, DuckDBPyRelation]

    def __init__(self, loader: Loader):
        self.loader = loader
        self.tables = {}

        self.db.sql('CREATE TABLE errors (rule_ref TEXT, error_type TEXT, object_id UINT64, val JSON);')
        self.errors = self.db.table('errors')

        for model_name, table in self.loader.tables.items():
            table = self._validate_model(self.models[model_name], table)
            table_name = f'"{model_name}.validated"'
            table.create(table_name)
            self.tables[model_name] = self.db.table(table_name)
    
    @property
    def db(self) -> DuckDBPyConnection:
        return self.loader.db
    
    @property
    def models(self) -> dict[TYPE_REF, Type]:
        return self.loader.models

    def _add_errors_where(self, r: DuckDBPyRelation, condition: str, rule_ref: str, error_type: str):
        err = r.filter(condition)
        err = err.select(f''' '{rule_ref}' as rule_ref, '{error_type}' as error_type, _index as object_id, to_json(val) as val''')
        err.insert_into('errors')
        return r.filter(f'''NOT ({condition})''')

    def check_for_index_collision(self, typ: Type, r: DuckDBPyRelation):
        packed_indexes = ','.join(f"list_pack({','.join(sorted(index))})" for index in typ.indexes)
        r = r.select(f'''_index, UNNEST([{packed_indexes}]) as index_val''')
        r = r.aggregate('index_val, list_distinct(list(_index)) as _indexes')

        r = r.select('index_val as val, unnest(_indexes) as _index, len(_indexes) > 1 as collision')

        self._add_errors_where(r,
            condition  = 'collision',
            rule_ref   = typ.ref, 
            error_type = 'NON_UNIQUE_INDEX'
        )
        # Select the good indexes
        return r.aggregate('_index, bool_or(collision) as collision').filter('not collision').select('_index')

    
    def _validate_model(self, typ: Type, r: DuckDBPyRelation):
        edges = r.aggregate('_index')

        # No need to check for conflicting indexes if there is only one
        if len(typ.indexes) > 1:
            edges = self.check_for_index_collision(typ, r)

        for edge in typ.edges:
            edge_rel = r.select(f'''_index, {edge if edge in r.columns else 'CAST(NULL as VARCHAR)'} as val''')
            edge_rel = self._validate_edge(typ, edge, edge_rel).set_alias(typ.ref + '.' + edge)
            edge_rel = edge_rel.select(f'''_index, val as {edge}''')
            edges = edges.join(edge_rel, '_index', how='left')
        return edges

    def _validate_edge(self, typ: Type, edge: EDGE, r: DuckDBPyRelation):
        agg_fun = 'list_distinct(flatten(list(val)))' if r.val.dtypes[0].id == 'list' else 'list_distinct(list(val))'
        r = r.aggregate(f'''_index, {agg_fun} as val''')

        if not typ.allows_null(edge):
            r = self._add_errors_where(r, 'len(val) == 0', typ.ref + '.' + edge, 'NOT_NULLABLE')
        
        if not typ.allows_multiple(edge):
            r = self._add_errors_where(r, 'len(val) > 1', typ.ref + '.' + edge, 'NOT_MULTIPLE')
            r = r.select(f'''_index, val[1] as val''')
        else:
            r = r.select(f'''_index, unnest(val) as val''')
        
        r = r.filter('val IS NOT NULL')
        r = self._validate_value(typ.get_edge(edge), r)

        if typ.allows_multiple(edge):
            r = r.aggregate('_index, list(val) as val')
        
        return r
    
    def _validate_value(self, typ: Type, r: DuckDBPyRelation):
        # TODO: Look up object references and see if they exist

        if typ.ref == 'User.name':
            length = COMPUTED_EDGES.apply(typ, 'length', r)
            print(length)
            print('meep')
        # if 'this is Boolean' in typ.assertions:
        #     r = self._add_errors_where(r, 'TRY_CAST(val as BOOLEAN) IS NULL', typ.ref, 'INVALID_VALUE')
        # if 'this is Number' in typ.assertions:
        #     r = self._add_errors_where(r, 'TRY_CAST(val AS DOUBLE) IS NULL', typ.ref, 'INVALID_VALUE')

        return r

    def __getitem__(self, model_name: TYPE_REF):
        return self.tables[model_name]
    
    def __repr__(self):
        return f"<Validate {','.join(self.tables.keys())}>"


class ComputedEdges:
    computations: dict[tuple[str,str], str]

    def __init__(self):
        self.computations = dict()
    
    def _get(self, typ: Type, edge: EDGE):
        assert typ.has_edge(edge)
        comp = self.computations.get((typ.ref, edge))
        if comp is None:
            if typ.extends and typ.extends.has_edge(edge):
                return self._get(typ.extends, edge)
        return comp
    
    def has(self, typ: Type, edge: EDGE):
        return self._get(typ, edge) is not None

    # allow multiple relations to be passed in
    # each being an argument to the function
    # then join each of the relations together?
    # but only if the other arguments are also indexes and not literals?
    def apply(self, typ: Type, edge: EDGE, r: DuckDBPyRelation):
        comp = self._get(typ, edge)
        return r.select(f'_index, {comp} as val')

    def set(self, type_ref: TYPE_REF, edge: EDGE, sql: str):
        assert (type_ref, edge) not in self.computations
        self.computations[(type_ref, edge)] = sql

COMPUTED_EDGES = ComputedEdges()
COMPUTED_EDGES.set('String','length', 'LENGTH(val)')

def expression(typ: Type, r: DuckDBPyRelation, expr: AST.Expression):
    assert isinstance(expr, AST.Expression)
    if isinstance(expr, AST.Identifier):
        if expr.kind == 'edge':
            edge = expr.name
            assert typ.has_edge(edge), f'Unknown edge: "{edge}"'
            edge_ref = typ.edge_origin(edge).ref + '.' + edge