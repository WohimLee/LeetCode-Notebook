from __future__ import annotations

import heapq
import random
from typing import List


class Solution:
    """解法一（推荐）：迭代版三路快选（Quickselect），平均 O(n)。

    思路：第 k 大 == 按升序排序后的第 len(nums) - k 个位置。
    使用三路划分（< pivot / == pivot / > pivot）可以优雅处理重复元素，
    全程用 while 循环，不使用递归。
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = nums[random.randint(left, right)]
            lt, i, gt = left, left, right

            # 划分后：
            # [left, lt)   < pivot
            # [lt, gt]     == pivot
            # (gt, right]  > pivot
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            if target < lt:
                right = lt - 1
            elif target > gt:
                left = gt + 1
            else:
                return nums[target]

        raise ValueError("invalid input")


class SolutionHeap:
    """解法二：维护大小为 k 的最小堆，时间 O(n log k)，空间 O(k)。

    堆顶始终是当前“前 k 大”里最小的那个，最后堆顶就是答案。
    适合数据流/无法整体排序的场景。
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap: list[int] = []

        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                heapq.heapreplace(heap, x)

        return heap[0]


class SolutionSort:
    """解法三：排序，时间 O(n log n)，代码最短、最稳定。"""

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


class SolutionCounting:
    """解法四：计数（桶）法，时间 O(n + range)。

    当数值范围不大时很好用。这里使用动态范围 [min(nums), max(nums)]，
    不依赖题目给出的固定边界。
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        lo, hi = min(nums), max(nums)
        count = [0] * (hi - lo + 1)

        for x in nums:
            count[x - lo] += 1

        rest = k
        for i in range(len(count) - 1, -1, -1):
            rest -= count[i]
            if rest <= 0:
                return i + lo

        raise ValueError("invalid input")
