from __future__ import annotations

from typing import List


class Solution:
    """迭代插入法：逐个数字插入到已有排列的每个位置。"""

    def permute(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = [[]]
        for x in nums:
            nxt: List[List[int]] = []
            for perm in res:
                for i in range(len(perm) + 1):
                    nxt.append(perm[:i] + [x] + perm[i:])
            res = nxt
        return res


class SolutionNextPermutation:
    """按字典序不断求 next_permutation（非递归）。"""

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        arr = sorted(nums)
        ans = [arr[:]]
        while self._next_permutation(arr):
            ans.append(arr[:])
        return ans

    def _next_permutation(self, arr: List[int]) -> bool:
        i = len(arr) - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i < 0:
            return False

        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]

        l, r = i + 1, len(arr) - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return True

