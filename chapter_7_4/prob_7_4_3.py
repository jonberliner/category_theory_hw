# implement reader functor
from typing import TypeVar, Callable

R = TypeVar('R')
A = TypeVar('A')
B = TypeVar('B')

G = Callable[[R,], A]
F = Callable[[A,], B]
H = Callable[[R,], B]

class ReaderFunctor(object):
    def __init__(self, r: R) -> None:
        self.r = r

    def __call__(self, f: F, g: G) -> H:
        def r_to_b(r: R) -> B:
            return f(g(r))
        return r_to_b

# example
def g(s: str) -> int:
    return len(s)

def f(i: int) -> bool:
    return i > 0

s_to_bool = ReaderFunctor(r=str)(f=f, g=g)

assert s_to_bool("hello") is True
assert s_to_bool("") is False
