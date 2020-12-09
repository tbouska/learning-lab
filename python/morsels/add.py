#!/bin/env/python3


def add(*args):
    result = []
    rows = 0
    columns = 0
    if not args[0]:
        raise ValueError("Nothing to add")
    for matrix in args:
        if rows == 0:
            rows = len(matrix)
        if rows != len(matrix):
            raise ValueError("Given matrices are not the same size")
        for i, row in enumerate(matrix):
            if columns == 0:
                columns = len(row)
            if columns != len(row):
                raise ValueError("Given matrices are not the same size")
            try:
                result[i]
            except IndexError:
                result.append([0]*len(row))
            for j, elem in enumerate(row):
                result[i][j] = result[i][j] + elem
    return result


if __name__ == "__main__":
    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    print(add(matrix1, matrix2))
    matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
    print(add(matrix1, matrix2))
    print(add([[1, 9], [7, 3]], [[5, -4], [3, 3]], [[2, 3], [-3, 1]],
              [[8, 8], [7, 7]]))
    print(add([[1, 9], [7, 3]], [[1, 2], [3]]))
