#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=35

The number, 197, is called a circular prime because all rotations of
the digits: 197, 971, and 719, are themselves prime. There are
thirteen such primes below 100:
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?

Answer: 55
"""
from __future__ import print_function
from utils import timer, is_prime, primes, rotate_digits, MILL, take_upto


ANSWER = 55


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    total = 0
    primes_less_limit = take_upto(MILL, primes())

    for p in primes_less_limit:
        n = p
        circular = True
        for _ in str(n):
            if not is_prime(n):
                circular = False
                break

            n = rotate_digits(n)

        if circular:
            total += 1

    return total


if __name__ == '__main__':
    print(main())
