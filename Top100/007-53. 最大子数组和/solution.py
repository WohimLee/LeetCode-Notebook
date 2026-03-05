# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """解法一（推荐）：Kadane，维护“以当前位置结尾”的最大和。"""

    # 定义 maxSubArray 函数/方法。
    def maxSubArray(self, nums: List[int]) -> int:
        # 初始化或更新变量 best。
        best = nums[0]
        # 初始化或更新变量 cur。
        cur = nums[0]

        # 遍历当前序列，逐步推进状态。
        for x in nums[1:]:
            # 初始化或更新变量 cur。
            cur = max(x, cur + x)
            # 初始化或更新变量 best。
            best = max(best, cur)
        # 返回当前函数结果。
        return best


# 定义 SolutionPrefixMin 类，封装该题解法。
class SolutionPrefixMin:
    """解法二：前缀和 + 历史最小前缀和。"""

    # 定义 maxSubArray 函数/方法。
    def maxSubArray(self, nums: List[int]) -> int:
        # 初始化或更新变量 prefix。
        prefix = 0
        # 初始化或更新变量 min_prefix。
        min_prefix = 0
        # 初始化或更新变量 ans。
        ans = nums[0]

        # 遍历当前序列，逐步推进状态。
        for x in nums:
            # 更新变量 prefix，推进当前状态。
            prefix += x
            # 初始化或更新变量 ans。
            ans = max(ans, prefix - min_prefix)
            # 初始化或更新变量 min_prefix。
            min_prefix = min(min_prefix, prefix)
        # 返回当前函数结果。
        return ans


# 定义 SolutionDPArray 类，封装该题解法。
class SolutionDPArray:
    """解法三：显式 DP 数组，便于初学者理解状态转移。"""

    # 定义 maxSubArray 函数/方法。
    def maxSubArray(self, nums: List[int]) -> int:
        # 初始化或更新变量 dp。
        dp = [0] * len(nums)
        # 初始化或更新变量 dp[0]。
        dp[0] = nums[0]
        # 初始化或更新变量 ans。
        ans = dp[0]

        # 遍历当前序列，逐步推进状态。
        for i in range(1, len(nums)):
            # 初始化或更新变量 dp[i]。
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            # 初始化或更新变量 ans。
            ans = max(ans, dp[i])
        # 返回当前函数结果。
        return ans
