from __future__ import annotations

from typing import Optional

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """迭代建 parent 映射，再回溯求最近公共祖先。"""

    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode',
    ) -> 'TreeNode':
        parent: dict[TreeNode, Optional[TreeNode]] = {root: None}
        stack = [root]

        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors: set[TreeNode] = set()
        cur: Optional[TreeNode] = p
        while cur is not None:
            ancestors.add(cur)
            cur = parent[cur]

        cur = q
        while cur not in ancestors:
            cur = parent[cur]
        return cur

