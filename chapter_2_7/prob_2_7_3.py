from random import Random

from prob_2_7_1 import memoize

def random_with_seed(seed: int) -> float:
    rng = Random(seed)
    return rng.random()

mrandom_with_seed = memoize(random_with_seed)

assert random_with_seed(1) == random_with_seed(1) == mrandom_with_seed(1) == mrandom_with_seed(1)
print("random with seed and memoized random with seed behave as expected (same value returned no matter how many times called, memoized or not")

# NOTE: when given a seed, rngs are deterministic, and so can be properly memoized for seed inputs
