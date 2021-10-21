def memoize(f):
    lookup = dict()
    def memoized(arg):
        if arg not in lookup:
            print(f"memoizing for arg {arg}")
            lookup[arg] = f(arg)
        return lookup[arg]
    return memoized
