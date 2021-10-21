def compose(f, g):
    def h(a):
        return g(f(a))
    return h
