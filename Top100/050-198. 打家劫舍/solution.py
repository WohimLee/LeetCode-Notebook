# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """滚动 DP。"""

    # 定义 rob 函数/方法。
    def rob(self, nums: List[int]) -> int:
        # 初始化或更新变量 prev2。
        prev2 = 0  # dp[i-2]
        # 初始化或更新变量 prev1。
        prev1 = 0  # dp[i-1]
        # 遍历当前序列，逐步推进状态。
        for x in nums:
            # 初始化或更新变量 prev2, prev1。
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        # 返回当前函数结果。
        return prev1


# 定义 SolutionDPArray 类，封装该题解法。
class SolutionDPArray:
    """显式 DP 数组，适合初学者理解状态转移。"""

    # 定义 rob 函数/方法。
    def rob(self, nums: List[int]) -> int:
        # 判断条件是否成立，选择对应处理分支。
        if not nums:
            # 返回当前函数结果。
            return 0
        # 判断条件是否成立，选择对应处理分支。
        if len(nums) == 1:
            # 返回当前函数结果。
            return nums[0]
        # 初始化或更新变量 dp。
        dp = [0] * len(nums)
        # 初始化或更新变量 dp[0]。
        dp[0] = nums[0]
        # 初始化或更新变量 dp[1]。
        dp[1] = max(nums[0], nums[1])
        # 遍历当前序列，逐步推进状态。
        for i in range(2, len(nums)):
            # 初始化或更新变量 dp[i]。
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        # 返回当前函数结果。
        return dp[-1]

