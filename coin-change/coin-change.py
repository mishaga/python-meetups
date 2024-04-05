def get_number() -> int:
    try:
        number = int(input('Enter a change sum: '))
    except ValueError:
        print('Enter a valid number, please')
        exit(1)

    if number <= 0:
        print('The number must be greater that zero')
        exit(1)

    return number


def find_all(value: int, nominals: tuple[int, ...], coins: list[int], solutions: list[list[int]]):
    if value == 0:
        solutions.append(coins)
        return

    if value < 0 or not nominals:
        return

    # left
    find_all(
        value=value - nominals[0],
        nominals=nominals,
        coins=coins + [nominals[0]],
        solutions=solutions,
    )

    # right
    find_all(
        value=value,
        nominals=nominals[1:],
        coins=coins[:],
        solutions=solutions,
    )


def find_shortest(solutions):
    min_len = None
    idx = None
    for i, val in enumerate(solutions):
        if min_len is None:
            min_len = len(val)
            idx = i
            continue
        if min_len > len(val):
            min_len = len(val)
            idx = i
    return idx


def main():
    number = get_number()
    solutions = []

    find_all(
        value=number,
        nominals=(9, 6, 5, 3, 1),
        coins=[],
        solutions=solutions,
    )
    # print(solutions)

    shortest_idx = find_shortest(solutions)
    print(shortest_idx, solutions[shortest_idx])


if __name__ == '__main__':
    main()
