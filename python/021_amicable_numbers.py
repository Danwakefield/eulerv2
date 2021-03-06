#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=21

Let d( n ) be defined as the sum of proper divisors of n (numbers less
than n which divide evenly into n ). If d( a ) = b and d( b ) = a ,
where a ≠ b , then a and b are an amicable pair and each of a and b
are called amicable numbers. For example, the proper divisors of 220
are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) =
284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) =
220. Evaluate the sum of all the amicable numbers under 10000.

Answer: 31626
"""
from __future__ import print_function
from utils import timer, factors
from functools import lru_cache


ANSWER = 31626


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@lru_cache(maxsize=None)
def factor_sum(n):
    return sum(factors(n, False))


@timer
def main():
    total = 0

    for n in range(2, 10001):
        b = factor_sum(n)
        if factor_sum(b) == n:
            if n != b:
                total += n

    return total


if __name__ == '__main__':
    print(main())
