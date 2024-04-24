from skyscraper_classes import Constraint, Matrix, Point, Points

SIZE = 4


def gen_empty_matrix(size: int) -> Matrix:
    return [
        [0] * size for _ in range(size)
    ]


def print_matrix(matrix: Matrix):
    print('')
    for line in matrix:
        for n in line:
            print(n, end=' ')
        print('')


def find_obvious(matrix: Matrix, constraints: Constraint) -> None:
    matrix[0][3] = 4
    matrix[2][0] = 4
    matrix[3][1] = 4
    # ...


def traverse_matrix(matrix: Matrix):
    stack: Points = [Point(x=0, y=0)]
    while stack:
        field = stack.pop()
        print('Field:', field, 'Value:', matrix[field.y][field.x])
        if field.x + 1 < SIZE:
            stack.append(Point(x=field.x + 1, y=field.y))
        if field.y + 1 < SIZE:
            stack.append(Point(x=field.x, y=field.y + 1))


def main():
    constraints = Constraint(
        top=(3, 2, 2, 1),
        right=(1, 2, 3, 2),
        bottom=(2, 1, 3, 3),
        left=(3, 2, 1, 2),
    )
    matrix: Matrix = gen_empty_matrix(size=SIZE)
    print_matrix(matrix)

    find_obvious(matrix=matrix, constraints=constraints)
    print_matrix(matrix)

    traverse_matrix(matrix=matrix)


if __name__ == '__main__':
    main()
