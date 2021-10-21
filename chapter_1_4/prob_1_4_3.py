from prob_1_4_1 import id
from prob_1_4_2 import compose

def add1(x):
    return x + 1

if __name__ == "__main__":
    f = id
    g = add1
    x = 1
    assert compose(f, f)(x) == x
    assert compose(f, g)(x) == g(x)
    assert compose(g, f)(x) == g(x)
    print("all tests pass")
