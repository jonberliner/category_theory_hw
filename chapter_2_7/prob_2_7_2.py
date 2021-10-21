from prob_2_7_1 import memoize
from random import uniform

def _uniform(args):
    return uniform(args[0], args[1])

def rand_fn_works(rand_fn, args):
    x0 = rand_fn(args)
    x1 = rand_fn(args)
    return x0 != x1

def print_result(rand_works_result):
    if rand_works_result:
        print("random works")
    else:
        print("got identical values on two calls - random function doesn't work")


if __name__ == "__main__":
    mrandom = memoize(_uniform)

    print("random.uniform test result:")
    print_result(rand_fn_works(_uniform, (1,2)))

    print("memoized random.uniform test result:")
    print_result(rand_fn_works(mrandom, (1, 2)))

    # NOTE: memoizing does not work for random functions
