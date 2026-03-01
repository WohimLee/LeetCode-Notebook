from __future__ import annotations

from typing import List


class Solution:
    """解法一（推荐）：Kadane，维护“以当前位置结尾”的最大和。"""

    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        cur = nums[0]

        for x in nums[1:]:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best


class SolutionPrefixMin:
    """解法二：前缀和 + 历史最小前缀和。"""

    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        min_prefix = 0
        ans = nums[0]

        for x in nums:
            prefix += x
            ans = max(ans, prefix - min_prefix)
            min_prefix = min(min_prefix, prefix)
        return ans


class SolutionDPArray:
    """解法三：显式 DP 数组，便于初学者理解状态转移。"""

    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        ans = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            ans = max(ans, dp[i])
        return ans
