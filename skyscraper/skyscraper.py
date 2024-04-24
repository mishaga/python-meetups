from typing import TypeAlias

mtrx: TypeAlias = list[list[int]]
cnstr: TypeAlias = tuple[tuple[int, ...], ...]


def gen_empty_matrix(size: int) -> mtrx:
    return [
        [0] * size for _ in range(size)
    ]


def print_matrix(matrix: mtrx):
    print('')
    for line in matrix:
        for n in line:
            print(n, end=' ')
        print('')


def find_obvious(matrix: mtrx, constraints: cnstr) -> None:
    matrix[0][3] = 4
    matrix[2][0] = 4
    matrix[3][1] = 4


def main():
    constraints: cnstr = (
        (3, 2, 2, 1),  # top
        (1, 2, 3, 2),  # right
        (2, 1, 3, 3),  # bottom
        (3, 2, 1, 2),  # left
    )
    matrix: mtrx = gen_empty_matrix(size=4)
    print_matrix(matrix)

    find_obvious(matrix=matrix, constraints=constraints)
    print_matrix(matrix)


if __name__ == '__main__':
    main()
