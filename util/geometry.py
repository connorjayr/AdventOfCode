from numbers import Number
from typing import Generic, Iterator, Tuple, TypeVar

T = TypeVar("T", bound=Number)


class Vector(Generic[T]):
    components: Tuple[T]

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

    def __init__(self, lower: Vector[T], upper: Vector[T]):
        if len(lower) != len(upper):
            raise ValueError("vectors must have same length")
        self.lower = lower
        self.upper = upper

    def __contains__(self, vec: Vector[T]) -> bool:
        return all(l <= x <= u for l, x, u in zip(self.lower, vec, self.upper))

    def expand(self, vec: Vector[T]):
        """Expands this bounding box to contain a vector.

        Args:
            vec: The vector.
        """
        self.lower = Vector[T](*(min(l, x) for l, x in zip(self.lower, vec)))
        self.upper = Vector[T](*(min(x, u) for x, u in zip(vec, self.upper)))
