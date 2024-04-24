from dataclasses import dataclass
from typing import TypeAlias

ConstraintLine: TypeAlias = tuple[int, ...]


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Constraint:
    top: ConstraintLine
    right: ConstraintLine
    bottom: ConstraintLine
    left: ConstraintLine


Matrix: TypeAlias = list[list[int]]
Points: TypeAlias = list[Point]
