from collections import deque
from typing import Optional, Generator

from trees.tree_class import TreeNode


def generate_tree() -> TreeNode:
    return TreeNode(
        'Menu',
        left=TreeNode(
            'Drinks',
            left=TreeNode(
                'Tea',
                left=TreeNode(
                    'Green',
                    left=TreeNode('Oolong'),
                    right=TreeNode('Da-hong-pao'),
                ),
                right=TreeNode(
                    'Black',
                    left=TreeNode('Georgia'),
                    right=TreeNode('India'),
                ),
            ),
            right=TreeNode(
                'Coffee',
                left=TreeNode('Brazil'),
                right=TreeNode('Arabica'),
            ),
        ),
        right=TreeNode(
            'Food',
            left=TreeNode(
                'Burgers',
                left=TreeNode('Beef-Burger'),
                right=TreeNode('Cheese-Burger'),
            ),
            right=TreeNode(
                'Pizza',
                left=TreeNode('Margarita'),
                right=TreeNode('Four-cheese'),
            ),
        ),
    )


def dfs(root: Optional[TreeNode]) -> Generator[str, None, None]:
    """Depth-first search."""
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

        yield node.data


def bfs(root: Optional[TreeNode]) -> Generator[str, None, None]:
    """Breadth-first search."""
    q = deque([root])
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if not node:
                continue

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            yield node.data


def main():
    tree = generate_tree()
    print('Depth-first search (DFS)')
    for data in dfs(root=tree):
        print(data, end=' ')

    print('\n')
    print('Breadth-first search (BFS)')
    for data in bfs(root=tree):
        print(data, end=' ')


if __name__ == '__main__':
    main()
