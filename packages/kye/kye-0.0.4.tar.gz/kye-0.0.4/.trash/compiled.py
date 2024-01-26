from __future__ import annotations
from typing import Union, Optional
from pydantic import BaseModel, constr, model_validator

TYPE = constr(pattern=r'[A-Z][a-z][a-zA-Z]*')
EDGE = constr(pattern=r'[a-z][a-z_]*')
TYPE_REF = constr(pattern=r'[A-Z][a-z][a-zA-Z]*(\.[A-Za-z]+)*')
EXPR = constr()

class ReferencedType(BaseModel):
    type: TYPE_REF
    filter: Optional[EXPR]

    def __repr__(self):
        return "Ref<{}{}>".format(
            self.type,
            '[' + self.filter + ']' if self.filter else '',
        )

class ExpressedType(BaseModel):
    expr: EXPR

    def __repr__(self):
        return "Expr<{}>".format(self.expr)

class ConstType(BaseModel):
    const: Union[str, int, float, bool]

    def __repr__(self):
        return "Const<{}>".format(repr(self.const))

Type = Union[ReferencedType, ExpressedType, ConstType]

class Edge(BaseModel):
    type: Type
    nullable: bool = False
    multiple: bool = False

    @model_validator(mode='before')
    @classmethod
    def validator(cls, data):
        if 'const' in data:
            data['type'] = ConstType(const=data['const'])
        if 'expr' in data:
            data['type'] = ExpressedType(expr=data['expr'])
        if 'type' in data:
            data['type'] = ReferencedType(type=data['type'], filter=data.get('filter'))
        return data

    def __repr__(self):
        return '{}{}'.format(
            super().__repr__(),
            ([['' ,'+'],
              ['?','*']])[int(self.nullable)][int(self.multiple)]
        )

class Model(BaseModel):
    type: Optional[TYPE_REF]
    indexes: list[list[EDGE]]
    edges: dict[EDGE, Edge]

    @classmethod
    def index_validator(cls, idx):
        if type(idx) is str:
            return [ idx ]
        elif type(idx) is list:
            assert len(idx) > 0
            for n in idx:
                assert type(n) is str
            return idx
        else:
            raise TypeError(f'Unexpected index type: {repr(idx)}')

    @model_validator(mode='before')
    @classmethod
    def validator(cls, data):
        if 'index' in data:
            assert 'indexes' not in data
            data['indexes'] = [ cls.index_validator(data['index']) ]
        elif 'indexes' in data:
            assert type(data['indexes']) is list
            assert len(data['indexes']) > 0
            data['indexes'] = [ cls.index_validator(idx) for idx in data['indexes'] ]
        return data

    def __getitem__(self, name: EDGE):
        return self.edges[name]

    def __contains__(self, name: EDGE):
        return name in self.edges

    def __repr__(self):
        all_indexes = [idx for idxs in self.indexes for idx in idxs]
        non_index_edges = [edge for edge in self.edges.keys() if edge not in all_indexes]
        return "Type<{}{}{}{}>".format(
            self.name or '',
            ':' + self.type if self.type else '',
            ''.join('(' + ','.join(idx) + ')' for idx in self.indexes),
            '{' + ','.join(non_index_edges) + '}' if len(non_index_edges) else '',
        )

class Dataset(BaseModel):
    models: dict[TYPE_REF, Union[Model, Type]] = {}
    
    def get(self, ref: TYPE_REF, default=None):
        return self.models.get(ref, default)
    
    def __getitem__(self, ref: TYPE_REF):
        return self.models[ref]

    def __contains__(self, ref: TYPE_REF):
        return ref in self.models

    def __repr__(self):
        return "Dataset<{}>".format(
            ','.join(self.models.keys()),
        )