# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """显式栈后序遍历：模拟递归计算每个节点向上贡献值。"""

    # 定义 maxPathSum 函数/方法。
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 判断条件是否成立，选择对应处理分支。
        if not root:
            # 返回当前函数结果。
            return 0

        # 初始化或更新变量 gain: dict[Optional[TreeNode], int]。
        gain: dict[Optional[TreeNode], int] = {None: 0}
        # 初始化或更新变量 ans。
        ans = float('-inf')
        # 初始化或更新关键状态变量。
        stack: list[tuple[Optional[TreeNode], bool]] = [(root, False)]

        # 当条件成立时循环处理，直到状态收敛。
        while stack:
            # 弹出元素用于回退或继续计算。
            node, visited = stack.pop()
            # 判断条件是否成立，选择对应处理分支。
            if node is None:
                # 跳过本轮剩余逻辑，进入下一轮循环。
                continue
            # 判断条件是否成立，选择对应处理分支。
            if not visited:
                # 向容器末尾追加元素，扩展结果集合。
                stack.append((node, True))
                # 向容器末尾追加元素，扩展结果集合。
                stack.append((node.right, False))
                # 向容器末尾追加元素，扩展结果集合。
                stack.append((node.left, False))
                # 跳过本轮剩余逻辑，进入下一轮循环。
                continue

            # 初始化或更新变量 left_gain。
            left_gain = max(gain[node.left], 0)
            # 初始化或更新变量 right_gain。
            right_gain = max(gain[node.right], 0)
            # 初始化或更新变量 ans。
            ans = max(ans, node.val + left_gain + right_gain)
            # 初始化或更新变量 gain[node]。
            gain[node] = node.val + max(left_gain, right_gain)

        # 返回当前函数结果。
        return int(ans)


# 定义 SolutionTwoStacks 类，封装该题解法。
class SolutionTwoStacks:
    """两栈拿到后序序列，再反向 DP。"""

    # 定义 maxPathSum 函数/方法。
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 判断条件是否成立，选择对应处理分支。
        if not root:
            # 返回当前函数结果。
            return 0

        # 初始化或更新变量 s1。
        s1 = [root]
        # 初始化或更新变量 order: list[TreeNode]。
        order: list[TreeNode] = []
        # 当条件成立时循环处理，直到状态收敛。
        while s1:
            # 弹出元素用于回退或继续计算。
            node = s1.pop()
            # 向容器末尾追加元素，扩展结果集合。
            order.append(node)
            # 判断条件是否成立，选择对应处理分支。
            if node.left:
                # 向容器末尾追加元素，扩展结果集合。
                s1.append(node.left)
            # 判断条件是否成立，选择对应处理分支。
            if node.right:
                # 向容器末尾追加元素，扩展结果集合。
                s1.append(node.right)

        # 初始化或更新变量 gain: dict[Optional[TreeNode], int]。
        gain: dict[Optional[TreeNode], int] = {None: 0}
        # 初始化或更新变量 ans。
        ans = float('-inf')
        # 遍历当前序列，逐步推进状态。
        for node in reversed(order):
            # 初始化或更新变量 left。
            left = max(gain[node.left], 0)
            # 初始化或更新变量 right。
            right = max(gain[node.right], 0)
            # 初始化或更新变量 ans。
            ans = max(ans, node.val + left + right)
            # 初始化或更新变量 gain[node]。
            gain[node] = node.val + max(left, right)
        # 返回当前函数结果。
        return int(ans)


if __name__ == "__main__":
    if "TreeNode" not in globals():
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    solution = Solution()
    print(solution.maxPathSum(root))
