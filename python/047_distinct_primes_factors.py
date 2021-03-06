#!/usr/bin/python3
# encoding: utf-8
"""
https://projecteuler.net/problem=47

The first two consecutive numbers to have two distinct prime factors
are:
    14 = 2 × 7
    15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors
are:
    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
"""
from __future__ import print_function
from utils import timer


ANSWER = None


def test_answer():
    if ANSWER is None:
        assert 0, 'Not Completed'
    else:
        assert ANSWER == main()


@timer
def main():
    pass


if __name__ == '__main__':
    print(main())
