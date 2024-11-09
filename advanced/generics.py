"""
This module demonstrates a generic Rose Tree implementation in Python using type parameters.

A Rose Tree is a tree data structure where each node can have any number of children. It consists of two types:
- Branch: A node that contains a list of subtrees
- Leaf: A terminal node containing a single value

The implementation uses Python's generic type syntax (PEP 695) with type parameters in square brackets.
Key features demonstrated:

- Generic type parameters [T], [A], [B] allowing the tree to store any type
- A RoseTree type alias representing the union of Branch and Leaf
- Dataclass decorators for clean class definitions
- A map() method that allows transforming the values in the tree from one type to another
- A print_tree() function that displays the tree structure with indentation

Example usage:
    Branch[int](                # Creates a tree of integers
        [
            Leaf(1),           # Leaf nodes with values
            Leaf(2),
            Branch([           # Nested branches
                Leaf(3),
                Leaf(4)
            ]),
            Branch([
                Leaf(5),
                Leaf(6)
            ]),
            Leaf(7)
        ]
    )

When printed, branches are shown with * and leaves with - followed by their value.
The map() method can transform the tree, e.g. converting numbers to strings.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Callable


type RoseTree[T] = Branch[T] | Leaf[T]


@dataclass
class Branch[A]:
    branches: list[RoseTree[A]]

    def map[B](self, f: Callable[[A], B]) -> Branch[B]:
        return Branch([b.map(f) for b in self.branches])


@dataclass
class Leaf[A]:
    value: A

    def map[B](self, f: Callable[[A], B]) -> Leaf[B]:
        return Leaf(f(self.value))


def print_tree[T](tree: RoseTree[T]) -> None:
    trees = [(tree, 0)]
    while trees:
        match trees.pop(0):
            case Branch(branches), level:
                print(" " * level * 2 + "*")
                trees = [(branch, level + 1) for branch in branches] + trees
            case Leaf(value), level:
                print(" " * level * 2 + "- " + repr(value))


example: Branch[int] = Branch(
    [
        Leaf(1),
        Leaf(2),
        Branch([Leaf(3), Leaf(4)]),
        Branch([Leaf(5), Leaf(6)]),
        Leaf(7),
    ]
)
print_tree(example.map(str))
