from __future__ import annotations

from typing import List


class Solution:
    """解法一（推荐）：排序 + 双指针，时间 O(n^2)。"""

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans: List[List[int]] = []

        for i in range(n - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue
            if x > 0:
                break

            l, r = i + 1, n - 1
            while l < r:
                s = x + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([x, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return ans


class SolutionHash:
    """解法二：固定第一个数 + 哈希去重，思路直观。"""

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans: List[List[int]] = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            seen: set[int] = set()
            used_second: set[int] = set()

            for j in range(i + 1, n):
                b = nums[j]
                c = target - b
                if c in seen and b not in used_second:
                    ans.append([nums[i], c, b])
                    used_second.add(b)
                seen.add(b)
        return ans
