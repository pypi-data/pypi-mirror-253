from __future__ import annotations
from typing import Literal, Optional, Generic, TypeVar
import re

TYPE_REF = str
EDGE_REF = str
        
class Expression:
    edge: EDGE_REF
    domain: TYPE_REF
    range: TYPE_REF
    params: list[TYPE_REF]
    args: list[Expression]

    def __init__(self,
                 edge: EDGE_REF,
                 domain: TYPE_REF,
                 range: TYPE_REF,
                 params: list[TYPE_REF] = [],
                 args: list[Expression] = []):
        assert len(params) == len(args)
        for arg, param in zip(args, params):
            assert arg.domain == domain
            assert arg.range == param
        self.edge = edge
        self.domain = domain
        self.range = range
        self.args = args

    @staticmethod
    def validate(typ: TYPE_REF):
        return Expression(edge=f'{typ}.is', domain='Any', range='Boolean')
    
    def literal(val):
        type_ref = None
        if type(val) is str:
            type_ref = 'String'
        if type(val) is int:
            type_ref = 'Number'
        if type(val) is float:
            type_ref = 'Number'
        if type(val) is bool:
            type_ref = 'Boolean'
        assert type_ref is not None, 'Unknown literal type'
        return Expression(
            edge=repr(val),
            domain='Any',
            range=type_ref,
        )

    def to(self, typ: TYPE_REF):
        if self.range == typ:
            return self
        return Expression(
            edge=f'{self.domain}.{typ}',
            domain=self.domain,
            range=typ,
        )

    def _logical(self, edge: str, other: Expression):
        assert isinstance(other, Expression)
        return Expression(
            edge=edge,
            domain=self.domain,
            range='Boolean',
            params=[ 'Boolean', 'Boolean' ],
            args=[ self.to('Boolean'), other.to('Boolean') ]
        )

    def __or__(self, other: Expression):
        return self._logical('or', other)

    def __and__(self, other: Expression):
        return self._logical('and', other)

    def __xor__(self, other: Expression):
        return self._logical('xor', other)
    
    def __repr__(self):
        return '{}{}'.format(
            self.edge,
            '(' + ','.join(repr(arg) for arg in self.args) + ')' if len(self.args) else '',
        )

number_or_string = Expression.validate('Number') | Expression.validate('String')

def compute(value, exp: Expression):
    args = [compute(value, arg) for arg in exp.args]


print('hi')