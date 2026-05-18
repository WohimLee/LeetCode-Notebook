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
            # 一路走到最左边，把沿途节点压栈，回退时再访问节点值。
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

            # 找到当前节点左子树里“中序遍历的前驱节点”。
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

if __name__ == "__main__":
    if "TreeNode" not in globals():
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    solution = Solution()
    print(solution.inorderTraversal(root))
