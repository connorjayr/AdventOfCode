from typing import Iterator, Tuple


class Vector:
    components: Tuple[int]

    def __init__(self, *components: int):
        self.components = components

    def __len__(self) -> int:
        return len(self.components)

    def __iter__(self) -> Iterator[int]:
        return iter(self.components)

    def __getitem__(self, key: int) -> int:
        return self.components[key]

    def __eq__(self, vec: "Vector") -> bool:
        return len(self) == len(vec) and all(x == y for x, y in zip(self, vec))

    def __ne__(self, vec: "Vector") -> bool:
        return not self == vec

    def __hash__(self) -> int:
        return hash(self.components)

    def __add__(self, vec: "Vector") -> "Vector":
        if len(self) != len(vec):
            return ValueError("vectors must have same length")
        return Vector(*(x + y for x, y in zip(self, vec)))

    def __mul__(self, scalar: int) -> "Vector":
        return Vector(*(x * scalar for x in self))

    def __neg__(self) -> "Vector":
        return -1 * self

    __rmul__ = __mul__

    def __sub__(self, vec: "Vector") -> "Vector":
        return self + -vec

    def __str__(self) -> str:
        return f"({', '.join(str(x) for x in self.components)})"

    def rotate_ccw(self) -> "Vector":
        """Rotates this vector 90 degrees counterclockwise.

        Returns:
            The rotated vector.

        Raises:
            ValueError: If this vector is not two-dimensional.
        """
        if len(self.components) != 2:
            raise ValueError("vector must be two-dimensional")
        return Vector(-self[1], self[0])

    def rotate_cw(self) -> "Vector":
        """Rotates this vector 90 degrees clockwise.

        Returns:
            The rotated vector.

        Raises:
            ValueError: If this vector is not two-dimensional.
        """
        if len(self.components) != 2:
            raise ValueError("vector must be two-dimensional")
        return Vector(self[1], -self[0])


UP = Vector(0, -1)
RIGHT = Vector(1, 0)
DOWN = Vector(0, 1)
LEFT = Vector(-1, 0)


class BoundingBox:
    lower: Vector
    upper: Vector

    def __init__(self, lower: Vector, upper: Vector):
        if len(lower) != len(upper):
            raise ValueError("vectors must have same length")
        self.lower = lower
        self.upper = upper

    def __contains__(self, vec: Vector) -> bool:
        return all(l <= x <= u for l, x, u in zip(self.lower, vec, self.upper))

    def expand(self, vec: Vector):
        """Expands this bounding box to contain a vector.

        Args:
            vec: The vector.
        """
        self.lower = Vector(*(min(l, x) for l, x in zip(self.lower, vec)))
        self.upper = Vector(*(min(x, u) for x, u in zip(vec, self.upper)))
