# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """经典迭代中序：显式栈。"""

    # 定义 inorderTraversal 函数/方法。
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 初始化或更新变量 ans: List[int]。
        ans: List[int] = []
        # 初始化或更新变量 stack: list[TreeNode]。
        stack: list[TreeNode] = []
        # 初始化或更新变量 cur。
        cur = root

        # 当条件成立时循环处理，直到状态收敛。
        while cur or stack:
            # 当条件成立时循环处理，直到状态收敛。
            while cur:
                # 向容器末尾追加元素，扩展结果集合。
                stack.append(cur)
                # 初始化或更新变量 cur。
                cur = cur.left
            # 弹出元素用于回退或继续计算。
            cur = stack.pop()
            # 向容器末尾追加元素，扩展结果集合。
            ans.append(cur.val)
            # 初始化或更新变量 cur。
            cur = cur.right
        # 返回当前函数结果。
        return ans


# 定义 SolutionMorris 类，封装该题解法。
class SolutionMorris:
    """Morris 遍历：O(1) 额外空间（会临时改指针）。"""

    # 定义 inorderTraversal 函数/方法。
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 初始化或更新变量 ans: List[int]。
        ans: List[int] = []
        # 初始化或更新变量 cur。
        cur = root
        # 当条件成立时循环处理，直到状态收敛。
        while cur:
            # 判断条件是否成立，选择对应处理分支。
            if not cur.left:
                # 向容器末尾追加元素，扩展结果集合。
                ans.append(cur.val)
                # 初始化或更新变量 cur。
                cur = cur.right
                # 跳过本轮剩余逻辑，进入下一轮循环。
                continue

            # 初始化或更新变量 pred。
            pred = cur.left
            # 当条件成立时循环处理，直到状态收敛。
            while pred.right and pred.right is not cur:
                # 初始化或更新变量 pred。
                pred = pred.right

            # 判断条件是否成立，选择对应处理分支。
            if not pred.right:
                # 初始化或更新变量 pred.right。
                pred.right = cur
                # 初始化或更新变量 cur。
                cur = cur.left
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 初始化或更新变量 pred.right。
                pred.right = None
                # 向容器末尾追加元素，扩展结果集合。
                ans.append(cur.val)
                # 初始化或更新变量 cur。
                cur = cur.right
        # 返回当前函数结果。
        return ans

