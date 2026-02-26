from __future__ import annotations

from typing import List


class Solution:
    """哈希集合：只从序列起点开始向后扩展。"""

    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for x in s:
            if x - 1 in s:
                continue
            y = x
            while y in s:
                y += 1
            ans = max(ans, y - x)
        return ans


class SolutionBoundaryMap:
    """边界长度合并：记录每段连续区间的左右边界长度。"""

    def longestConsecutive(self, nums: List[int]) -> int:
        length: dict[int, int] = {}
        ans = 0
        for x in nums:
            if x in length:
                continue
            left = length.get(x - 1, 0)
            right = length.get(x + 1, 0)
            cur = left + 1 + right
            length[x] = cur
            length[x - left] = cur
            length[x + right] = cur
            ans = max(ans, cur)
        return ans

