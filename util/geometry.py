import itertools
import math
from numbers import Number
from typing import Generic, Iterator, TypeVar

T = TypeVar("T", bound=Number)


class Vector(Generic[T]):
    components: tuple[T]

    def __init__(self, *components: T):
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
        return f"({', '.join(str(x) for x in self.components)})"

    __repr__ = __str__

    def adjacent(self, include_corners=False, step=1) -> Iterator["Vector[T]"]:
        """
        Args:
            include_corners: Whether or not to consider corners as adjacent.
            step: The step size between this vector and adjacent ones.

        Returns:
            An iterator that iterates through all vectors adjacent to this
            vector.
        """
        if include_corners:
            for offset in itertools.product((-step, 0, step), repeat=len(self)):
                if all(x == 0 for x in offset):
                    # A vector cannot be adjacent to itself
                    continue
                yield self + Vector(*offset)
        else:
            for component_idx in range(len(self)):
                for offset in (-step, step):
                    yield self + Vector(
                        *(
                            offset if idx == component_idx else 0
                            for idx in range(len(self))
                        )
                    )

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
        self.lower = lower
        self.upper = upper

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
        self.upper = Vector[T](*(min(x, u) for x, u in zip(vec, self.upper)))

    def integral_points(self) -> Iterator[Vector[T]]:
        lower = Vector[int](*(math.ceil(x) for x in self.lower))
        upper = Vector[int](*(math.floor(x) for x in self.upper))
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
