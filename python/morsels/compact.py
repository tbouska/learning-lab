#!/usr/bin/env python3
# compact.py
""" This is my solution to compact Morsel """

SENTINEL = object()


def compact(seq):
    """ Returns iterable from sequence where adjacent duplicates are removed
    """
    prev = SENTINEL
    for val in seq:
        if prev != val:
            prev = val
            yield val


if __name__ == "__main__":
    print(list(compact([1, 1, 2, 2, 3, 2])))
    print(list(compact(n**2 for n in [1, 2, 2])))
    c = compact(n**2 for n in [1, 2, 2])
    print(iter(c) is c)
