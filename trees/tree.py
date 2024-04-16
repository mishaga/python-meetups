from typing import Any, Self, Generator


class TreeNode:

    def __init__(self, data: Any, left: Self | None = None, right: Self | None = None):
        self.data = data
        self.left = left
        self.right = right


def get_tree() -> TreeNode:
    food = TreeNode(data='Food', left=TreeNode('Burger'), right=TreeNode('Pizza'))
    drinks = TreeNode(data='Drinks', left=TreeNode('Tea'), right=TreeNode('Coffee'))
    return TreeNode(data='Menu', left=drinks, right=food)


def recursive_without_tco(root: TreeNode | None, list_to_add: list):
    if not root:
        return
    list_to_add.append(root.data)
    recursive_without_tco(root.left, list_to_add)
    recursive_without_tco(root.right, list_to_add)


def tree_to_list(root: TreeNode | None) -> list[TreeNode]:
    stack = [root]
    lst = []
    while stack:
        node = stack.pop()
        if node:
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            lst.append(node.data)
    return lst


def tree_traversal_gen(root: TreeNode | None) -> Generator[str, None, None]:
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        if node:
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            yield node.data


def recursive_with_tco(stack: list[TreeNode]) -> list[str]:
    if len(stack) == 0:
        return []

    node = stack.pop()
    if node:
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        return [node.data] + recursive_with_tco(stack)

    return recursive_with_tco(stack)


def recursive_with_tco_optimised(stack: list[TreeNode]) -> list[str]:
    if len(stack) == 0:
        return []

    node = stack.pop()
    if node.right:
        stack.append(node.right)
    if node.left:
        stack.append(node.left)

    return [node.data] + recursive_with_tco_optimised(stack)


def recursive_with_tco_gen(stack: list[TreeNode]) -> Generator[str, None, None]:
    if len(stack) != 0:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

        yield node.data
        yield from recursive_with_tco_gen(stack)


def main():
    tree = get_tree()
    lst = tree_to_list(tree)
    print(lst)

    print(list(recursive_with_tco_gen([tree])))

    # lst = recursive_with_tco([tree])
    # print(lst)

    # without_tco_lst = []
    # recursive_without_tco(tree, without_tco_lst)
    # print(without_tco_lst)

    # without_tco_lst = []
    # recursive_without_tco(tree, without_tco_lst)
    # print(without_tco_lst)

    # for node_data in tree_traversal_gen(tree):
    #     print(node_data, end=' ')


if __name__ == '__main__':
    main()
