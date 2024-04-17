from typing import Any, Self


class TreeNode:

    def __init__(self, data: Any):
        self.data = data

    @property
    def left(self) -> Self | None:
        if self.data - 1 < 0:
            return None
        return TreeNode(self.data - 1)

    @property
    def right(self) -> Self | None:
        if self.data - 2 < 0:
            return None
        return TreeNode(self.data - 2)


def print_tree(root: TreeNode):
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def main():
    root = TreeNode(3)
    print_tree(root)

    sum_ = 0
    stack = [root]
    while stack:
        node = stack.pop()
        sum_ += node.data
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    print('SUM:', sum_)


if __name__ == '__main__':
    main()
