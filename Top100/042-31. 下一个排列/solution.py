from __future__ import annotations

from typing import List

class Solution:
    """标准 next_permutation。"""

    def nextPermutation(self, nums: List[int]) -> None:
        # 从右向左找第一个升序对，位置 i 就是“枢轴”。
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # 再从右侧找第一个比 nums[i] 大的数与之交换。
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 枢轴右侧原本是降序，反转后就是最小升序后缀。
        l, r = i + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

class SolutionSortSuffix:
    """同一思路的直观版本：交换后对后缀排序。"""

    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1 :] = sorted(nums[i + 1 :])

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    solution.nextPermutation(nums)
    print(nums)
