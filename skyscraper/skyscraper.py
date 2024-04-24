def main():
    matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    print_matrix(matrix)


def print_matrix(matrix):
    print('')
    for line in matrix:
        for n in line:
            print(n, end=' ')
        print('')


if __name__ == '__main__':
    main()
