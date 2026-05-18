from __future__ import annotations

from typing import List

class Solution:
    """动态维护“以当前位置结尾”的最大乘积和最小乘积。"""

    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = ans = nums[0]
        for x in nums[1:]:
            if x < 0:
                # 乘上负数后，最大值和最小值会互换角色。
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(x, cur_max * x)
            cur_min = min(x, cur_min * x)
            ans = max(ans, cur_max)
        return ans

class SolutionPrefixSuffix:
    """前后各扫一遍，处理被 0 切开的区间。"""

    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        prod = 1
        for x in nums:
            prod *= x
            ans = max(ans, prod)
            if x == 0:
                # 0 会把连续乘积截断，后面需要重新开始计算。
                prod = 1
        prod = 1
        for x in reversed(nums):
            prod *= x
            ans = max(ans, prod)
            if x == 0:
                prod = 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct([2, 3, -2, 4]))
