from __future__ import annotations

from typing import List


class Solution:
    """双指针：每次移动较短板。"""

    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            h = min(height[l], height[r])
            ans = max(ans, h * (r - l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans

