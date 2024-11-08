"""
Pattern matching and expression evaluator example that demonstrates a simple interpreter.

This module implements a small expression evaluator with the following features:
- Basic expressions: integers, booleans, and variable references
- Binary operations: < and > comparisons between integers
- Let expressions for binding values to variables
- If expressions for conditional evaluation

Types:
- Expr: Union type representing valid expressions (int, bool, str, BinOp, Let, If)
- Env: Dictionary mapping variable names to their values
- Value: Union type for possible evaluation results (int, bool)

The eval() function evaluates expressions using pattern matching to handle different cases:
- Literals (int, bool) evaluate to themselves
- Variables (str) look up values in the environment
- Let expressions create new bindings in a new environment
- Binary operations compare two integers
- If expressions evaluate conditionally based on a boolean condition

Example usage:
    Let("x", 1, If(BinOp("<", "x", 2), 42, 0))
    # Binds x=1, checks if x<2 (true), returns 42
"""

from typing import Literal
from dataclasses import dataclass

type Expr = int | bool | str | BinOp | Let | If


@dataclass
class BinOp:
    """
    Represents a binary operation expression between two values.
    Supports comparison operations '<' and '>' between integer values.
    """

    op: Literal["<"] | Literal[">"]
    lhs: Expr
    rhs: Expr


@dataclass
class Let:
    """
    Represents a let-binding expression that introduces a new variable binding.
    A Let expression evaluates the value expression, binds it to the given name in a new
    environment, then evaluates the body expression in that extended environment.
    """

    name: str
    value: Expr
    body: Expr


@dataclass
class If:
    """
    Represents a conditional if-then-else expression.
    Evaluates the condition and returns the result of evaluating either the
    'then' expression or the 'else' expression based on the condition.
    """

    cond: Expr
    t: Expr
    f: Expr


type Env = dict[str, Value]
type Value = int | bool


def eval(env: Env, expr: Expr) -> Value:
    match expr:
        case int() | bool():
            return expr
        case str():
            return env[expr]
        case Let(name, value, body):
            new_env = env | {name: eval(env, value)}
            return eval(new_env, body)

        case BinOp(op, lhs, rhs):
            left = eval(env, lhs)
            right = eval(env, rhs)
            match op, left, right:
                case "<", int(), int():
                    return left < right
                case ">", int(), int():
                    return left > right
                case _:
                    raise ValueError(
                        f"Invalid binary operation {op} on {lhs} and {rhs}"
                    )

        case If(cond, t, f):
            match eval(env, cond):
                case True:
                    return eval(env, t)
                case False:
                    return eval(env, f)
                case c:
                    raise ValueError(f"Expected bool condition, got: {c}")


example = Let("x", 1, If(BinOp("<", "x", 2), 42, 0))
print(eval({}, example))
