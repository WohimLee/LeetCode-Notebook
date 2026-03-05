# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """双指针：每次移动较短板。"""

    # 定义 maxArea 函数/方法。
    def maxArea(self, height: List[int]) -> int:
        # 初始化或更新变量 l, r。
        l, r = 0, len(height) - 1
        # 初始化或更新变量 ans。
        ans = 0
        # 当条件成立时循环处理，直到状态收敛。
        while l < r:
            # 初始化或更新变量 h。
            h = min(height[l], height[r])
            # 初始化或更新变量 ans。
            ans = max(ans, h * (r - l))
            # 判断条件是否成立，选择对应处理分支。
            if height[l] <= height[r]:
                # 更新变量 l，推进当前状态。
                l += 1
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 更新变量 r，推进当前状态。
                r -= 1
        # 返回当前函数结果。
        return ans

