#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=45

Triangle, pentagonal, and hexagonal numbers are generated by the
following formulae:
    Triangle T_n = n(n+1)/2      1, 3, 6, 10, 15, ...
    Pentagonal P_n = n(3n−1)/2   1, 5, 12, 22, 35, ...
    Hexagonal H_n = n(2n−1)      1, 6, 15, 28, 45, ...
It can be verified that T_285 = P_165 = H_143 = 40755.
Find the next triangle number that is also
pentagonal and hexagonal.

Answer: 1533776805
"""
from __future__ import print_function
from utils import timer, is_pentagonal_number, drop_n, hex_numbers_gen


ANSWER = 1533776805


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    # All hexagonal numbers are also triangular so we dont need to check them
    # if we use them as a base.
    # Start from H_144 as we are asked for the next one.
    for h in drop_n(144, hex_numbers_gen()):
        if is_pentagonal_number(h):
            return h


if __name__ == '__main__':
    print(main())
