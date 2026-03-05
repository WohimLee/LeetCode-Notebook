# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """动态维护“以当前位置结尾”的最大乘积和最小乘积。"""

    # 定义 maxProduct 函数/方法。
    def maxProduct(self, nums: List[int]) -> int:
        # 初始化或更新变量 cur_max。
        cur_max = cur_min = ans = nums[0]
        # 遍历当前序列，逐步推进状态。
        for x in nums[1:]:
            # 判断条件是否成立，选择对应处理分支。
            if x < 0:
                # 初始化或更新变量 cur_max, cur_min。
                cur_max, cur_min = cur_min, cur_max
            # 初始化或更新变量 cur_max。
            cur_max = max(x, cur_max * x)
            # 初始化或更新变量 cur_min。
            cur_min = min(x, cur_min * x)
            # 初始化或更新变量 ans。
            ans = max(ans, cur_max)
        # 返回当前函数结果。
        return ans


# 定义 SolutionPrefixSuffix 类，封装该题解法。
class SolutionPrefixSuffix:
    """前后各扫一遍，处理被 0 切开的区间。"""

    # 定义 maxProduct 函数/方法。
    def maxProduct(self, nums: List[int]) -> int:
        # 初始化或更新变量 ans。
        ans = nums[0]
        # 初始化或更新变量 prod。
        prod = 1
        # 遍历当前序列，逐步推进状态。
        for x in nums:
            # 更新变量 prod，推进当前状态。
            prod *= x
            # 初始化或更新变量 ans。
            ans = max(ans, prod)
            # 判断条件是否成立，选择对应处理分支。
            if x == 0:
                # 初始化或更新变量 prod。
                prod = 1
        # 初始化或更新变量 prod。
        prod = 1
        # 遍历当前序列，逐步推进状态。
        for x in reversed(nums):
            # 更新变量 prod，推进当前状态。
            prod *= x
            # 初始化或更新变量 ans。
            ans = max(ans, prod)
            # 判断条件是否成立，选择对应处理分支。
            if x == 0:
                # 初始化或更新变量 prod。
                prod = 1
        # 返回当前函数结果。
        return ans

