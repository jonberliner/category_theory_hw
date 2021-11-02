# implement Haskell's `Either` fn as a generic type
from typing import TypeVar, Callable

T1 = TypeVar('T1')
T2 = TypeVar('T2')
T3 = TypeVar('T3')


class Either(object):
    def __init__(self,
            t1: T1,
            t2: T2,
            left: Callable[[T1], T3],
            right: Callable[[T2], T3],
        ) -> None:

        self.t1 = t1
        self.t2 = t2
        self.left = left
        self.right = right

    def __call__(self,
            t: type) -> T3:
        if isinstance(t, self.t1):
            return self.left(t)
        elif isinstance(t, self.t2):
            return self.right(t)
        else:
            raise TypeError(f"invalid type {t}. type must be {self.t1} or {self.t2}")
