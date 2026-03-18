# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """二分划分：在较短数组上二分切分位置。"""

    # 定义 findMedianSortedArrays 函数/方法。
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 判断条件是否成立，选择对应处理分支。
        if len(nums1) > len(nums2):
            # 初始化或更新变量 nums1, nums2。
            nums1, nums2 = nums2, nums1

        # 初始化或更新变量 m, n。
        m, n = len(nums1), len(nums2)
        # 初始化或更新变量 total_left。
        total_left = (m + n + 1) // 2
        # 初始化或更新变量 left, right。
        left, right = 0, m

        # 当条件成立时循环处理，直到状态收敛。
        while left <= right:
            # 初始化或更新变量 i。
            i = (left + right) // 2
            # 初始化或更新变量 j。
            j = total_left - i

            # 执行当前语句，更新算法状态。
            l1 = float('-inf') if i == 0 else nums1[i - 1]
            # 执行当前语句，更新算法状态。
            r1 = float('inf') if i == m else nums1[i]
            # 执行当前语句，更新算法状态。
            l2 = float('-inf') if j == 0 else nums2[j - 1]
            # 执行当前语句，更新算法状态。
            r2 = float('inf') if j == n else nums2[j]

            # 判断条件是否成立，选择对应处理分支。
            if l1 <= r2 and l2 <= r1:
                # 判断条件是否成立，选择对应处理分支。
                if (m + n) % 2 == 1:
                    # 返回当前函数结果。
                    return float(max(l1, l2))
                # 返回当前函数结果。
                return (max(l1, l2) + min(r1, r2)) / 2.0
            # 判断条件是否成立，选择对应处理分支。
            if l1 > r2:
                # 初始化或更新变量 right。
                right = i - 1
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 初始化或更新变量 left。
                left = i + 1

        # 主动抛出异常，提示输入或状态不合法。
        raise ValueError('Invalid input arrays')


# 定义 SolutionKth 类，封装该题解法。
class SolutionKth:
    """迭代删除第 k 小元素的一半区间。"""

    # 定义 findMedianSortedArrays 函数/方法。
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 初始化或更新变量 m, n。
        m, n = len(nums1), len(nums2)

        # 定义 kth 函数/方法。
        def kth(k: int) -> int:
            # 初始化或更新变量 i。
            i = j = 0
            # 当条件成立时循环处理，直到状态收敛。
            while True:
                # 判断条件是否成立，选择对应处理分支。
                if i == m:
                    # 返回当前函数结果。
                    return nums2[j + k - 1]
                # 判断条件是否成立，选择对应处理分支。
                if j == n:
                    # 返回当前函数结果。
                    return nums1[i + k - 1]
                # 判断条件是否成立，选择对应处理分支。
                if k == 1:
                    # 返回当前函数结果。
                    return min(nums1[i], nums2[j])

                # 初始化或更新变量 half。
                half = k // 2
                # 初始化或更新变量 ni。
                ni = min(i + half, m) - 1
                # 初始化或更新变量 nj。
                nj = min(j + half, n) - 1
                # 判断条件是否成立，选择对应处理分支。
                if nums1[ni] <= nums2[nj]:
                    # 更新变量 k，推进当前状态。
                    k -= ni - i + 1
                    # 初始化或更新变量 i。
                    i = ni + 1
                # 执行上述条件均不满足时的兜底逻辑。
                else:
                    # 更新变量 k，推进当前状态。
                    k -= nj - j + 1
                    # 初始化或更新变量 j。
                    j = nj + 1

        # 初始化或更新变量 a。
        a = kth((m + n + 1) // 2)
        # 初始化或更新变量 b。
        b = kth((m + n + 2) // 2)
        # 返回当前函数结果。
        return (a + b) / 2.0


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 3], [2]))
