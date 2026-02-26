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

