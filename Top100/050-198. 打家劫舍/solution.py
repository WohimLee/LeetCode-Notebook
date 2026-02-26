from __future__ import annotations

from typing import List


class Solution:
    """滚动 DP。"""

    def rob(self, nums: List[int]) -> int:
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        for x in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        return prev1


class SolutionDPArray:
    """显式 DP 数组，适合初学者理解状态转移。"""

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

