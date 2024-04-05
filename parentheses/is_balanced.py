def is_balanced(line: str) -> bool:
    counter = 0
    for char in line:
        if char == ')' and counter == 0:
            return False

        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1

    return counter == 0


def main():
    assert is_balanced('(') is False
    assert is_balanced(')') is False
    assert is_balanced(')(') is False
    assert is_balanced('()') is True
    assert is_balanced('())') is False
    assert is_balanced('()(') is False
    assert is_balanced('(()') is False
    assert is_balanced(')()') is False
    assert is_balanced('(()))') is False
    assert is_balanced('()()()()') is True
    assert is_balanced('abc()') is True
    assert is_balanced('(qwe)') is True
    assert is_balanced('(qwerty()()()') is False


if __name__ == '__main__':
    main()
    print('done')
