"""Number sequence generators for use in Project Euler problems"""
import itertools as it


def primes():
    """Prime Generator"""
    # http://stackoverflow.com/a/3796442
    D = {9: 3, 25: 5}
    yield 2
    yield 3
    yield 5
    MASK = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,)
    MODULOS = frozenset((1, 7, 11, 13, 17, 19, 23, 29))

    for q in it.compress(it.islice(it.count(7), 0, None, 2), it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D or (x % 30) not in MODULOS:
                x += 2*p
            D[x] = p


def factor_pairs(n):
    """Generate the factor pairs of N"""
    for div in range(1, int(n ** 0.5) + 1):
        if n % div == 0:
            yield [div, n//div]


def _factor_pairs_v2(n):
    """Generate the factor pairs of N"""
    for div in range(1, int(n ** 0.5) + 1):
        if n % div == 0:
            yield div
            yield n//div


def factors(n, include_n=True):
    s = set(_factor_pairs_v2(n))

    if not include_n:
        s.discard(n)
    return s


def fib():
    """Fibonnaci Number generator"""
    a, b = 1, 1

    yield 1
    yield 1

    while True:
        f = a + b
        a = b
        b = f
        yield f


def square_numbers_gen():
    n = 1
    while True:
        x = n * n
        yield x
        n += 1


def tri_numbers_gen():
    n = 1
    while True:
        x = (n * (n + 1)) / 2
        yield int(x)
        n += 1


def pent_numbers_gen():
    n = 1
    while True:
        x = ((3 * n**2) - n) / 2
        yield int(x)
        n += 1


def hex_numbers_gen():
    n = 1
    while True:
        x = (2 * n**2) - n
        yield int(x)
        n += 1


def hept_numbers_gen():
    n = 1
    while True:
        x = ((5 * n**2) - (3 * n)) / 2
        yield int(x)
        n += 1


def oct_numbers_gen():
    n = 1
    while True:
        x = (3 * n**2) - (2 * n)
        yield int(x)
        n += 1
