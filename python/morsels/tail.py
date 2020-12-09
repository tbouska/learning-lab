#!/bin/env/python3

def tail(iterable, n):
    iterator = iter(iterable)
    tail = []
    while n > 0:
        try:
            tail.insert(0, next(iterator))
        except StopIteration:
            tail.reverse()
            return tail
        else:
            if len(tail) > n:
                tail.pop()
    return tail

if __name__ == "__main__":
    print(tail([1, 2, 3, 4, 5], 3))
    print(tail('hello', 2))
    print(tail('hello', 0))
    print(tail('hello', -2))
    squares = (n**2 for n in range(10))
    print(tail(squares, 3))
