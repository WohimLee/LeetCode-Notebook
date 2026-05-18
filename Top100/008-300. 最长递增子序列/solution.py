from __future__ import annotations

from bisect import bisect_left
from typing import List

class Solution:
    """解法一（推荐）：贪心 + 二分（牌堆法），时间 O(n log n)。"""

    def lengthOfLIS(self, nums: List[int]) -> int:
        tails: list[int] = []

        for x in nums:
            # tails[i] 维护“长度为 i+1 的递增子序列”的最小结尾。
            i = bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)

class SolutionDP:
    """解法二：经典 DP，dp[i] 表示以 i 结尾的 LIS 长度。"""

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n
        ans = 1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    # 尝试把 nums[i] 接到所有更小的 nums[j] 后面。
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(solution.lengthOfLIS(nums))
