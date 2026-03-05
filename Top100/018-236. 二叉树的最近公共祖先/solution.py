# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import Optional

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """迭代建 parent 映射，再回溯求最近公共祖先。"""

    # 定义 lowestCommonAncestor 函数/方法。
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode',
    ) -> 'TreeNode':
        # 初始化或更新关键状态变量。
        parent: dict[TreeNode, Optional[TreeNode]] = {root: None}
        # 初始化或更新变量 stack。
        stack = [root]

        # 当条件成立时循环处理，直到状态收敛。
        while p not in parent or q not in parent:
            # 弹出元素用于回退或继续计算。
            node = stack.pop()
            # 判断条件是否成立，选择对应处理分支。
            if node.left:
                # 初始化或更新变量 parent[node.left]。
                parent[node.left] = node
                # 向容器末尾追加元素，扩展结果集合。
                stack.append(node.left)
            # 判断条件是否成立，选择对应处理分支。
            if node.right:
                # 初始化或更新变量 parent[node.right]。
                parent[node.right] = node
                # 向容器末尾追加元素，扩展结果集合。
                stack.append(node.right)

        # 初始化或更新变量 ancestors: set[TreeNode]。
        ancestors: set[TreeNode] = set()
        # 初始化或更新变量 cur: Optional[TreeNode]。
        cur: Optional[TreeNode] = p
        # 当条件成立时循环处理，直到状态收敛。
        while cur is not None:
            # 调用函数/方法，推进当前步骤。
            ancestors.add(cur)
            # 初始化或更新变量 cur。
            cur = parent[cur]

        # 初始化或更新变量 cur。
        cur = q
        # 当条件成立时循环处理，直到状态收敛。
        while cur not in ancestors:
            # 初始化或更新变量 cur。
            cur = parent[cur]
        # 返回当前函数结果。
        return cur

