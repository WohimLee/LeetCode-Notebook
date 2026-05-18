from __future__ import annotations

from collections import defaultdict
from typing import List

class Solution:
    """前缀和 + 计数哈希表。"""

    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        prefix = 0
        ans = 0
        for x in nums:
            prefix += x
            # 若此前出现过 prefix-k，就说明存在若干子数组以当前位置结尾且和为 k。
            ans += cnt[prefix - k]
            cnt[prefix] += 1
        return ans

class SolutionPrefixBrute:
    """前缀和 + 双循环（易理解，O(n^2)）。"""

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n + 1):
                if prefix[j] - prefix[i] == k:
                    ans += 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraySum([1, 1, 1], 2))
