import itertools
import math
from numbers import Number
from typing import Generic, Iterator, Optional, TypeVar

T = TypeVar("T", bound=Number)


class Vector(Generic[T]):
    components: tuple[T]

    def __init__(self, *components: T) -> "Vector[T]":
        self.components = components

    def __len__(self) -> T:
        return len(self.components)

    def __iter__(self) -> Iterator[T]:
        return iter(self.components)

    def __getitem__(self, key: T) -> T:
        return self.components[key]

    def __eq__(self, vec: "Vector[T]") -> bool:
        return len(self) == len(vec) and all(x == y for x, y in zip(self, vec))

    def __ne__(self, vec: "Vector[T]") -> bool:
        return not self == vec

    def __hash__(self) -> T:
        return hash(self.components)

    def __add__(self, vec: "Vector[T]") -> "Vector[T]":
        if len(self) != len(vec):
            return ValueError("vectors must have same length")
        return Vector[T](*(x + y for x, y in zip(self, vec)))

    def __mul__(self, scalar: T) -> "Vector[T]":
        return Vector[T](*(x * scalar for x in self))

    def __neg__(self) -> "Vector[T]":
        return -1 * self

    __rmul__ = __mul__

    def __sub__(self, vec: "Vector[T]") -> "Vector[T]":
        return self + -vec

    def __str__(self) -> str:
        return f"({', '.join(str(x) for x in self)})"

    __repr__ = __str__

    def neighbors(
        self, include_diagonal=False, in_bbox: "Optional[BoundingBox[T]]" = None, step=1
    ) -> Iterator["Vector[T]"]:
        """
        Args:
            include_diagonal: Whether or not to include vectors that are one
            step away diagonally in the return values.
            step: The step size between this vector and its neighbors.

        Returns:
            An iterator that iterates through the neighbors of this vector.
        """
        if include_diagonal:
            for offset in itertools.product((-step, 0, step), repeat=len(self)):
                if all(x == 0 for x in offset):
                    # A vector cannot be neighbors with itself
                    continue
                neighbor = self + Vector(*offset)
                if in_bbox is not None and neighbor not in in_bbox:
                    continue
                yield neighbor
        else:
            for component_idx in range(len(self)):
                for offset in (-step, step):
                    neighbor = self + Vector(
                        *(
                            offset if idx == component_idx else 0
                            for idx in range(len(self))
                        )
                    )
                    if in_bbox is not None and neighbor not in in_bbox:
                        continue
                    yield neighbor

    def rotate_ccw(self) -> "Vector[T]":
        """Rotates this vector 90 degrees counterclockwise.

        Returns:
            The rotated vector.

        Raises:
            ValueError: If this vector is not two-dimensional.
        """
        if len(self.components) != 2:
            raise ValueError("vector must be two-dimensional")
        return Vector[T](-self[1], self[0])

    def rotate_cw(self) -> "Vector[T]":
        """Rotates this vector 90 degrees clockwise.

        Returns:
            The rotated vector.

        Raises:
            ValueError: If this vector is not two-dimensional.
        """
        if len(self.components) != 2:
            raise ValueError("vector must be two-dimensional")
        return Vector[T](self[1], -self[0])


UP = Vector[int](0, -1)
RIGHT = Vector[int](1, 0)
DOWN = Vector[int](0, 1)
LEFT = Vector[int](-1, 0)


class BoundingBox(Generic[T]):
    lower: Vector[T]
    upper: Vector[T]

    def __init__(self, lower: Vector[T], upper: Vector[T]) -> "BoundingBox[T]":
        if len(lower) != len(upper):
            raise ValueError("vectors must have same length")
        self.lower = Vector[T](*(min(l, u) for l, u in zip(lower, upper)))
        self.upper = Vector[T](*(max(l, u) for l, u in zip(lower, upper)))

    @classmethod
    def from_grid(cls, grid: list[any]) -> "BoundingBox[T]":
        """Constructs a bounding box containing all positions in an
        n-dimensional list.

        Args:
            grid: The n-dimensional list.

        Returns:
            The bounding box.
        """
        components = list[int]()
        while isinstance(grid, list):
            components.append(len(grid) - 1)
            grid = grid[0]
        upper = Vector[int](*components)
        return cls(upper - upper, upper)

    def __contains__(self, vec: Vector[T]) -> bool:
        return all(l <= x <= u for l, x, u in zip(self.lower, vec, self.upper))

    def expand(self, vec: Vector[T]):
        """Expands this bounding box to contain a vector.

        Args:
            vec: The vector.
        """
        self.lower = Vector[T](*(min(l, x) for l, x in zip(self.lower, vec)))
        self.upper = Vector[T](*(max(x, u) for x, u in zip(vec, self.upper)))

    def integral_points(self) -> Iterator[Vector[T]]:
        lower = Vector[int](*(math.ceil(l) for l in self.lower))
        upper = Vector[int](*(math.floor(u) for u in self.upper))
        yield from map(
            lambda x: Vector[int](*x),
            itertools.product(*(range(l, u + 1) for l, u in zip(lower, upper))),
        )


class Line:
    endpoints: tuple[Vector[int]]

    def __init__(self, a: Vector[int], b: Vector[int]):
        if len(a) != 2 or len(b) != 2:
            raise ValueError("endpoints must be two-dimensional")
        self.endpoints = (a, b)

    def slope(self) -> Vector[int]:
        """
        Returns:
            The slope of this line.
        """
        num = self.endpoints[1].components[1] - self.endpoints[0].components[1]
        denom = self.endpoints[1].components[0] - self.endpoints[0].components[0]
        gcd = math.gcd(num, denom)
        return Vector[int](num // gcd, denom // gcd)

    def integral_points(self) -> Iterator[Vector[int]]:
        """
        Returns:
            An iterator that iterates over the integral points (points whose
            coordinates are both integers) through which this line passes.
        """
        point = self.endpoints[0]
        yield point

        step = Vector[int](*reversed(self.slope()))
        while point != self.endpoints[1]:
            point += step
            yield point
