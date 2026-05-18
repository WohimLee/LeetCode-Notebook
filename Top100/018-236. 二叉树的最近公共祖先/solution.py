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
        # parent 记录每个节点的父节点，方便从任意点向上回溯。
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
        # 第一个同时出现在 p 祖先链上的节点，就是最近公共祖先。
        while cur not in ancestors:
            cur = parent[cur]
        return cur

if __name__ == "__main__":
    if "TreeNode" not in globals():
        class TreeNode:
            def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None

    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    p = root.left
    q = root.left.right.right
    solution = Solution()
    lca = solution.lowestCommonAncestor(root, p, q)
    print(lca.val if lca else None)
