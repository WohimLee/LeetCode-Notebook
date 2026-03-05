# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """双指针：较低的一侧决定当前能接多少水。"""

    # 定义 trap 函数/方法。
    def trap(self, height: List[int]) -> int:
        # 初始化或更新变量 l, r。
        l, r = 0, len(height) - 1
        # 初始化或更新变量 left_max。
        left_max = right_max = 0
        # 初始化或更新变量 ans。
        ans = 0

        # 当条件成立时循环处理，直到状态收敛。
        while l < r:
            # 判断条件是否成立，选择对应处理分支。
            if height[l] <= height[r]:
                # 初始化或更新变量 left_max。
                left_max = max(left_max, height[l])
                # 更新变量 ans，推进当前状态。
                ans += left_max - height[l]
                # 更新变量 l，推进当前状态。
                l += 1
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 初始化或更新变量 right_max。
                right_max = max(right_max, height[r])
                # 更新变量 ans，推进当前状态。
                ans += right_max - height[r]
                # 更新变量 r，推进当前状态。
                r -= 1
        # 返回当前函数结果。
        return ans


# 定义 SolutionStack 类，封装该题解法。
class SolutionStack:
    """单调栈：当前柱子作为右边界结算凹槽。"""

    # 定义 trap 函数/方法。
    def trap(self, height: List[int]) -> int:
        # 初始化或更新变量 stack: list[int]。
        stack: list[int] = []
        # 初始化或更新变量 ans。
        ans = 0
        # 遍历当前序列，逐步推进状态。
        for i, h in enumerate(height):
            # 当条件成立时循环处理，直到状态收敛。
            while stack and h > height[stack[-1]]:
                # 弹出元素用于回退或继续计算。
                mid = stack.pop()
                # 判断条件是否成立，选择对应处理分支。
                if not stack:
                    # 终止当前循环，进入后续流程。
                    break
                # 初始化或更新变量 left。
                left = stack[-1]
                # 初始化或更新变量 width。
                width = i - left - 1
                # 初始化或更新变量 bounded_height。
                bounded_height = min(height[left], h) - height[mid]
                # 更新变量 ans，推进当前状态。
                ans += width * bounded_height
            # 向容器末尾追加元素，扩展结果集合。
            stack.append(i)
        # 返回当前函数结果。
        return ans

