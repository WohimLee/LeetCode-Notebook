from __future__ import annotations

from collections import deque
from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """BFS 层序遍历。"""

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q: deque[TreeNode] = deque([root])
        ans: List[List[int]] = []
        while q:
            level_size = len(q)
            level: List[int] = []
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans


class SolutionIterativeDFS:
    """迭代 DFS（栈 + 深度）。"""

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans: List[List[int]] = []
        stack: list[tuple[TreeNode, int]] = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if depth == len(ans):
                ans.append([])
            ans[depth].append(node.val)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        return ans

