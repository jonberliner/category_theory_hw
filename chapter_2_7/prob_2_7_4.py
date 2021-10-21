from prob_2_7_1 import memoize

# Which of these fns are pure?  Try to memoize them and observe what happens with you call them multiple times: memoized and not.

def memoize_works_same_as_unmemoized(f, *args) -> bool:
    mf = memoize(f)

    f0 = f(*args)
    f1 = f(*args)

    mf0 = mf(*args)
    mf1 = mf(*args)
    mfdet = f0 == f1

    works_same = f0 == mf0 and f1 == mf1
    return works_same

# 4a
## factorial fn
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

## NOTE: no side effects or randomness, so fact is pure and should memoize just fine
print(f"memoization works for factorial?: {memoize_works_same_as_unmemoized(fact, 6)}")

## 4c
# NOTE: don't know what this means in C++.  if the std changes on each call, memo won't work.  if it doesn't it will work.  it looks like there are side effects to std::cout on each call, so we have side effects and so the won't work

## 4d
# NOTE: not pure (internal state y changes) so memoization won't work
# NOTE: 4b will be the same, as there is an internal changing state that memoize will not track
def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(y=0)
def f(x: int) -> int:
    f.y += x
    return f.y

print(f"memoization works for f counter?: {memoize_works_same_as_unmemoized(f, 2)}")
