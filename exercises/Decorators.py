#!/usr/bin/env python3

# -------------
# Decorators.py
# -------------

def cache_1 (f) :
    def g (n) :
        return f(n)
    return g

@cache_1
def cycle_length_1 (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class cache_2 :
    def __init__ (self, f) :
        self.f = f

    def __call__ (self, n) :
        return self.f(n)

@cache_2
def cycle_length_2 (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

def test (f) :
    assert f( 1) == 1
    assert f( 5) == 6
    assert f(10) == 7

print("Decorators.py")

test(cycle_length_1)
test(cycle_length_2)

print("Done.")