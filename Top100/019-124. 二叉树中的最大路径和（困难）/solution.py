from __future__ import annotations

from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """显式栈后序遍历：模拟递归计算每个节点向上贡献值。"""

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        gain: dict[Optional[TreeNode], int] = {None: 0}
        ans = float('-inf')
        stack: list[tuple[Optional[TreeNode], bool]] = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
                continue

            left_gain = max(gain[node.left], 0)
            right_gain = max(gain[node.right], 0)
            ans = max(ans, node.val + left_gain + right_gain)
            gain[node] = node.val + max(left_gain, right_gain)

        return int(ans)


class SolutionTwoStacks:
    """两栈拿到后序序列，再反向 DP。"""

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        s1 = [root]
        order: list[TreeNode] = []
        while s1:
            node = s1.pop()
            order.append(node)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)

        gain: dict[Optional[TreeNode], int] = {None: 0}
        ans = float('-inf')
        for node in reversed(order):
            left = max(gain[node.left], 0)
            right = max(gain[node.right], 0)
            ans = max(ans, node.val + left + right)
            gain[node] = node.val + max(left, right)
        return int(ans)

