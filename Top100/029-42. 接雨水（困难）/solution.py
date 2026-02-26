from __future__ import annotations

from typing import List


class Solution:
    """双指针：较低的一侧决定当前能接多少水。"""

    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        ans = 0

        while l < r:
            if height[l] <= height[r]:
                left_max = max(left_max, height[l])
                ans += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                ans += right_max - height[r]
                r -= 1
        return ans


class SolutionStack:
    """单调栈：当前柱子作为右边界结算凹槽。"""

    def trap(self, height: List[int]) -> int:
        stack: list[int] = []
        ans = 0
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                mid = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                bounded_height = min(height[left], h) - height[mid]
                ans += width * bounded_height
            stack.append(i)
        return ans

