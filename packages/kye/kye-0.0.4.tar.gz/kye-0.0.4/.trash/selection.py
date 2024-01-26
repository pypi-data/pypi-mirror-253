from __future__ import annotations
from typing import Optional, Union, Any, Literal
from pydantic import BaseModel, constr, model_validator
from dataclasses import dataclass, field

TYPE_REF = str
EDGE_REF = str

MESSAGES = {
    '.length.gt(Number)' : 'must be longer than {} characters',
    '.length.gte(Number)': 'must be at least {} characters long',
    '.length.le(Number)' : 'must be shorter than {} characters',
    '.length.lte(Number)': 'must be at most {} characters long',
    '.length.eq(Number)' : 'must be {} characters long',
    '.length.ne(Number)' : 'can\'t be {} characters long',
}

@dataclass
class Condition:
    type: Optional[TYPE_REF] = None
    msg: Optional[str] = None
    # loc: TokenPosition

class ConditionGroup(Condition):
    conditions: list[Condition]
    operator: Literal['and','or','xor']

    def __post_init__(self):
        assert len(self.conditions) >= 2
        for cond in self.conditions:
            assert isinstance(cond, Condition)
        assert self.operator in ('and','or','xor')
        
        types = {cond.type for cond in self.conditions}
        if len(types) == 1:
            self.type = list(types)[0]

class Function(Condition):
    edge: EDGE_REF
    type: TYPE_REF
    args: list[Function] = field(default_factory=list)

    def __repr__(self):
        if len(self.args) == 0:
            return self.edge
        if len(self.args) == 1:
            return '{}.{}'.format(
                repr(self.args[0]) if self.args[0].edge != 'this' else '',
                self.edge,
            )
        if len(self.args) > 1:
            return '{}.{}({})'.format(
                repr(self.args[0]) if self.args[0].edge != 'this' else '',
                self.edge,
                ','.join(repr(arg) for arg in self.args[1:])
            )
    
    def call(self, edge: EDGE_REF, returns=TYPE_REF, args: list[Function] = []):
        return Function(
            edge=edge,
            type=returns,
            args=[self, *args]
        )

@dataclass
class Selection:
    formats: list[TYPE_REF]
    conditions: list[Condition] = field(default_factory=list)

    def add_condition(self, condition: Condition):
        assert isinstance(condition, Condition)
        return Selection(
            type= self.type,
            conditions= self.conditions + [ condition ]
        )

    def compare_literal(self, op: str, other: Constant):
        return self.add_condition(Condition(
            exp=Function(
                edge=op,
                type='Boolean',
                args=[
                    Function('this', type=self.type),
                    other
                ],
            )
        ))
    
    def this(self):
        return Function('this', type=self.type)

@dataclass
class Constant:
    weight = 0
    type: TYPE_REF
    value: Union[str, float, int, bool]

    def __init__(self, value):
        if type(value) is str:
            self.type = 'String'
        if isinstance(value, (int, float)):
            self.type = 'Number'
        if type(value) is bool:
            self.type = 'Boolean'
        assert self.type is not None, 'Unknown value type'
        self.value = value
    
    def __repr__(self):
        return repr(self.value)

    def call(self, edge: EDGE_REF, returns=TYPE_REF, args: list[Constant] = []):
        for arg in args:
            assert isinstance(arg, Constant)
        # TODO: Compute the new value, since it is just another literal

Expression = Union[Composite, Selection, Function, Constant]

def apply_operation(op: str, rhs: Expression, lhs: Expression):
    sig = (rhs.__class__, lhs.__class__)
    if sig == (Composite, Selection) and op in ('or', 'xor') and rhs.exclusive == (op == 'xor'):
        return rhs.add_selection(lhs)
    if sig == (Selection, Constant) and op in ('lt', 'gt', 'lte', 'gte', 'eq', 'ne'):
        return rhs.compare_literal(op, lhs)

if __name__ == '__main__':
    # num = Selection('Number').compare_literal('gt', Literal(4))
    # String = Selection('String')
    # big_string = String.add_condition(Condition(
    #     exp=String.this()\
    #         .call('length', returns='Number')\
    #         .call('gt', args=[Literal(4)], returns='Boolean'),
    #     msg='String must be longer than 4 characters',
    # ))
    apply_operation('gt', Selection('Number'), Constant(4))
    print('hi')