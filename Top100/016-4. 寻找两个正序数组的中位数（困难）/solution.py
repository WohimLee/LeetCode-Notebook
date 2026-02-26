from __future__ import annotations

from typing import List


class Solution:
    """二分划分：在较短数组上二分切分位置。"""

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = total_left - i

            l1 = float('-inf') if i == 0 else nums1[i - 1]
            r1 = float('inf') if i == m else nums1[i]
            l2 = float('-inf') if j == 0 else nums2[j - 1]
            r2 = float('inf') if j == n else nums2[j]

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 1:
                    return float(max(l1, l2))
                return (max(l1, l2) + min(r1, r2)) / 2.0
            if l1 > r2:
                right = i - 1
            else:
                left = i + 1

        raise ValueError('Invalid input arrays')


class SolutionKth:
    """迭代删除第 k 小元素的一半区间。"""

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        def kth(k: int) -> int:
            i = j = 0
            while True:
                if i == m:
                    return nums2[j + k - 1]
                if j == n:
                    return nums1[i + k - 1]
                if k == 1:
                    return min(nums1[i], nums2[j])

                half = k // 2
                ni = min(i + half, m) - 1
                nj = min(j + half, n) - 1
                if nums1[ni] <= nums2[nj]:
                    k -= ni - i + 1
                    i = ni + 1
                else:
                    k -= nj - j + 1
                    j = nj + 1

        a = kth((m + n + 1) // 2)
        b = kth((m + n + 2) // 2)
        return (a + b) / 2.0

