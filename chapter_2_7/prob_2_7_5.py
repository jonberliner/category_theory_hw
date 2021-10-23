## how many different functions are there from Bool or Bool?
### ANSWER: four functions: x -> x and x -> !x, always true, always false

## implement
def id(x: bool) -> bool:
    return x

def inv(x: bool) -> bool:
    return not x

def true(x: bool) -> bool:
    return True

def false(x: bool) -> bool:
    return False
