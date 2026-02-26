from __future__ import annotations

from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """经典迭代中序：显式栈。"""

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans: List[int] = []
        stack: list[TreeNode] = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans


class SolutionMorris:
    """Morris 遍历：O(1) 额外空间（会临时改指针）。"""

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans: List[int] = []
        cur = root
        while cur:
            if not cur.left:
                ans.append(cur.val)
                cur = cur.right
                continue

            pred = cur.left
            while pred.right and pred.right is not cur:
                pred = pred.right

            if not pred.right:
                pred.right = cur
                cur = cur.left
            else:
                pred.right = None
                ans.append(cur.val)
                cur = cur.right
        return ans

