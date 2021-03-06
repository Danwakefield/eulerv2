#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13. What is the 10 001st prime number?

Answer: 104743
"""
from __future__ import print_function
from utils import timer, primes, drop_n
from itertools import islice


ANSWER = 104743


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    return next(drop_n(10000, primes()))


if __name__ == '__main__':
    print(main())
