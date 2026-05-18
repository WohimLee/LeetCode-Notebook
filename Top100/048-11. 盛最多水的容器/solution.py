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
            # 移动较短板才有机会让容器高度变大。
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
