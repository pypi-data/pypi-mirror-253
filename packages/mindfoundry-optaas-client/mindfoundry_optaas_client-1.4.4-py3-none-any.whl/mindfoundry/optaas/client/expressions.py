import abc


class Expression(abc.ABC):
    """Allows us to build expressions for :class:`Constraints <.Constraint>` using common operators.
    The following operators are supported:
        * addition: `x + y`
        * subtraction: `x - y`
        * multiplication: `x * y`
        * division: `x / y`
        * floor division: `x // y`
        * remainder: `x % y`
        * exponentiation: `x ** y`
        * equality: `x == y`
        * inequality: `x != y`
        * greater than: `x > y`
        * greater than or equal: `x >= y`
        * less than: `x < y`
        * less than or equal: `x <= y`
        * and: `x & y`
        * or: `x | y`

    Example:
        `((param1 + param2 <= param3) & param4.is_present()) | param5 == 'abc'`

    Note the use of brackets with the `&` and `|` operators - this is because they don't have the same precedence as
    `and` and `or` so you need to be explicit in order to generate the correct expression.


    See `this page <../constraints.ipynb>`_ for more examples.

    Refer to the OPTaaS swagger page for more details on constraint syntax.
    """

    def __add__(self, other) -> 'Expression':
        return BinaryPredicate(self, '+', other)

    def __radd__(self, other) -> 'Expression':
        return BinaryPredicate(other, '+', self)

    def __sub__(self, other) -> 'Expression':
        return BinaryPredicate(self, '-', other)

    def __rsub__(self, other) -> 'Expression':
        return BinaryPredicate(other, '-', self)

    def __mul__(self, other) -> 'Expression':
        return BinaryPredicate(self, '*', other)

    def __rmul__(self, other) -> 'Expression':
        return BinaryPredicate(other, '*', self)

    def __truediv__(self, other) -> 'Expression':
        return BinaryPredicate(self, '/', other)

    def __rtruediv__(self, other) -> 'Expression':
        return BinaryPredicate(other, '/', self)

    def __floordiv__(self, other) -> 'Expression':
        return BinaryPredicate(self, '//', other)

    def __rfloordiv__(self, other) -> 'Expression':
        return BinaryPredicate(other, '//', self)

    def __mod__(self, other) -> 'Expression':
        return BinaryPredicate(self, '%', other)

    def __rmod__(self, other) -> 'Expression':
        return BinaryPredicate(other, '%', self)

    def __pow__(self, other) -> 'Expression':
        return BinaryPredicate(self, '**', other)

    def __rpow__(self, other) -> 'Expression':
        return BinaryPredicate(other, '**', self)

    def __eq__(self, other) -> 'Expression':  # type: ignore
        return BinaryPredicate(self, '==', other)

    def __ne__(self, other) -> 'Expression':  # type: ignore
        return BinaryPredicate(self, '!=', other)

    def __gt__(self, other) -> 'Expression':
        return BinaryPredicate(self, '>', other)

    def __lt__(self, other) -> 'Expression':
        return BinaryPredicate(self, '<', other)

    def __ge__(self, other) -> 'Expression':
        return BinaryPredicate(self, '>=', other)

    def __le__(self, other) -> 'Expression':
        return BinaryPredicate(self, '<=', other)

    def __and__(self, other) -> 'Expression':
        return BinaryPredicate(self, '&&', other)

    def __or__(self, other) -> 'Expression':
        return BinaryPredicate(self, '||', other)

    @abc.abstractmethod
    def to_optaas_expression(self) -> str:
        pass


class Predicate(Expression):
    """An Expression that evaluates to a boolean value that can be used in a :class:`.Constraint`"""

    def __init__(self, optaas_expression: str) -> None:
        self._optaas_expression = optaas_expression

    def to_optaas_expression(self) -> str:
        """A string representation of this expression in a format which can be parsed by OPTaaS"""
        return self._optaas_expression


class BinaryPredicate(Predicate):
    """A Predicate with 2 operands"""

    def __init__(self, left_operand, operator: str, right_operand) -> None:
        super().__init__(f'{_format(left_operand)} {operator} {_format(right_operand)}')


class UnaryPredicate(Predicate):
    """A Predicate with a single operand"""

    def __init__(self, operand, operator: str) -> None:
        super().__init__(f'{_format(operand)} {operator}')


class WhenThenExpression(abc.ABC):
    """
    Defines a when expression, then expression clause:

    The "when" part is optional (if omitted, the then part applies).

    NOTE: At the MFOpt level, WhenThenExpressions get transformed to either constraints or prior mean functions, which
    means the "then" expressions have to conform to some formats: they have to be boolean for constraints, and not
    boolean for prior means.
    """
    def __init__(self, then: Expression, when: Expression = None) -> None:
        self.then = then
        self.when = when

    def to_optaas_expression(self) -> str:
        return (self.then.to_optaas_expression() if self.when is None
                else f'if {self.when.to_optaas_expression()} then {self.then.to_optaas_expression()}')

    def __eq__(self, other):
        return isinstance(other, WhenThenExpression) and self.to_optaas_expression() == other.to_optaas_expression()

    def __repr__(self):
        return self.to_optaas_expression()


class Constraint(WhenThenExpression):
    """
    This is an alias for the WhenThenExpression class which defines a when expression, then expression clause:

    The "when" part is optional (if omitted, the then part applies).
    """
    def __eq__(self, other):
        return isinstance(other, Constraint) and self.to_optaas_expression() == other.to_optaas_expression()


class PriorMeanExpression(WhenThenExpression):
    """
    This is an alias for the WhenThenExpression class which defines a when expression, then expression clause:

    The "when" part is optional (if omitted, the then part applies).
    """
    def __eq__(self, other):
        return isinstance(other, PriorMeanExpression) and self.to_optaas_expression() == other.to_optaas_expression()


def _format(operand):
    from mindfoundry.optaas.client.parameter import Parameter  # pylint: disable=import-outside-toplevel
    if operand is True:
        operand = 'true'
    elif operand is False:
        operand = 'false'
    elif isinstance(operand, Parameter):
        operand = operand.to_optaas_expression()
    elif isinstance(operand, str):
        operand = f"'{operand}'"
    elif isinstance(operand, BinaryPredicate):
        operand = '( ' + operand.to_optaas_expression() + ' )'
    elif isinstance(operand, UnaryPredicate):
        operand = operand.to_optaas_expression()
    return operand
