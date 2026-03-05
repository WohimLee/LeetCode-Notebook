# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from collections import deque
# 导入当前解法依赖的模块或类型。
from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """BFS 层序遍历。"""

    # 定义 levelOrder 函数/方法。
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 判断条件是否成立，选择对应处理分支。
        if not root:
            # 返回当前函数结果。
            return []

        # 初始化或更新变量 q: deque[TreeNode]。
        q: deque[TreeNode] = deque([root])
        # 初始化或更新变量 ans: List[List[int]]。
        ans: List[List[int]] = []
        # 当条件成立时循环处理，直到状态收敛。
        while q:
            # 初始化或更新变量 level_size。
            level_size = len(q)
            # 初始化或更新变量 level: List[int]。
            level: List[int] = []
            # 遍历当前序列，逐步推进状态。
            for _ in range(level_size):
                # 从队列头部弹出元素，按 FIFO 顺序处理。
                node = q.popleft()
                # 向容器末尾追加元素，扩展结果集合。
                level.append(node.val)
                # 判断条件是否成立，选择对应处理分支。
                if node.left:
                    # 向容器末尾追加元素，扩展结果集合。
                    q.append(node.left)
                # 判断条件是否成立，选择对应处理分支。
                if node.right:
                    # 向容器末尾追加元素，扩展结果集合。
                    q.append(node.right)
            # 向容器末尾追加元素，扩展结果集合。
            ans.append(level)
        # 返回当前函数结果。
        return ans


# 定义 SolutionIterativeDFS 类，封装该题解法。
class SolutionIterativeDFS:
    """迭代 DFS（栈 + 深度）。"""

    # 定义 levelOrder 函数/方法。
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 判断条件是否成立，选择对应处理分支。
        if not root:
            # 返回当前函数结果。
            return []

        # 初始化或更新变量 ans: List[List[int]]。
        ans: List[List[int]] = []
        # 初始化或更新变量 stack: list[tuple[TreeNode, int]]。
        stack: list[tuple[TreeNode, int]] = [(root, 0)]
        # 当条件成立时循环处理，直到状态收敛。
        while stack:
            # 弹出元素用于回退或继续计算。
            node, depth = stack.pop()
            # 判断条件是否成立，选择对应处理分支。
            if depth == len(ans):
                # 向容器末尾追加元素，扩展结果集合。
                ans.append([])
            # 向容器末尾追加元素，扩展结果集合。
            ans[depth].append(node.val)
            # 判断条件是否成立，选择对应处理分支。
            if node.right:
                # 向容器末尾追加元素，扩展结果集合。
                stack.append((node.right, depth + 1))
            # 判断条件是否成立，选择对应处理分支。
            if node.left:
                # 向容器末尾追加元素，扩展结果集合。
                stack.append((node.left, depth + 1))
        # 返回当前函数结果。
        return ans

