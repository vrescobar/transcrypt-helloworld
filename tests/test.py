#!/usr/bin/env python3

from typing import Iterator

def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


def test_nothing():
    assert list(fib(9)) == [0, 1, 1, 2, 3, 5, 8]
