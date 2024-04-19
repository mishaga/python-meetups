from typing import Any, Self


class TreeNode:

    def __init__(self, data: Any, left: Self | None = None, right: Self | None = None):
        self.data = data
        self.left = left
        self.right = right
