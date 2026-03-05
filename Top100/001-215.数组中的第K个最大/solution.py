# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
import heapq
# 导入当前解法依赖的模块或类型。
import random
# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """解法一（推荐）：迭代版三路快选（Quickselect），平均 O(n)。

    # 执行当前语句，更新算法状态。
    思路：第 k 大 == 按升序排序后的第 len(nums) - k 个位置。
    # 执行当前语句，更新算法状态。
    使用三路划分（< pivot / == pivot / > pivot）可以优雅处理重复元素，
    # 执行当前语句，更新算法状态。
    全程用 while 循环，不使用递归。
    """

    # 定义 findKthLargest 函数/方法。
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 初始化或更新变量 target。
        target = len(nums) - k
        # 初始化或更新变量 left, right。
        left, right = 0, len(nums) - 1

        # 当条件成立时循环处理，直到状态收敛。
        while left <= right:
            # 初始化或更新变量 pivot。
            pivot = nums[random.randint(left, right)]
            # 初始化或更新变量 lt, i, gt。
            lt, i, gt = left, left, right

            # 划分后：
            # [left, lt)   < pivot
            # [lt, gt]     == pivot
            # (gt, right]  > pivot
            while i <= gt:
                # 判断条件是否成立，选择对应处理分支。
                if nums[i] < pivot:
                    # 初始化或更新变量 nums[lt], nums[i]。
                    nums[lt], nums[i] = nums[i], nums[lt]
                    # 更新变量 lt，推进当前状态。
                    lt += 1
                    # 更新变量 i，推进当前状态。
                    i += 1
                # 当前置条件不满足时，继续判断该分支条件。
                elif nums[i] > pivot:
                    # 初始化或更新变量 nums[gt], nums[i]。
                    nums[gt], nums[i] = nums[i], nums[gt]
                    # 更新变量 gt，推进当前状态。
                    gt -= 1
                # 执行上述条件均不满足时的兜底逻辑。
                else:
                    # 更新变量 i，推进当前状态。
                    i += 1

            # 判断条件是否成立，选择对应处理分支。
            if target < lt:
                # 初始化或更新变量 right。
                right = lt - 1
            # 当前置条件不满足时，继续判断该分支条件。
            elif target > gt:
                # 初始化或更新变量 left。
                left = gt + 1
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 返回当前函数结果。
                return nums[target]

        # 主动抛出异常，提示输入或状态不合法。
        raise ValueError("invalid input")


# 定义 SolutionHeap 类，封装该题解法。
class SolutionHeap:
    """解法二：维护大小为 k 的最小堆，时间 O(n log k)，空间 O(k)。

    # 执行当前语句，更新算法状态。
    堆顶始终是当前“前 k 大”里最小的那个，最后堆顶就是答案。
    # 执行当前语句，更新算法状态。
    适合数据流/无法整体排序的场景。
    """

    # 定义 findKthLargest 函数/方法。
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 初始化或更新变量 heap: list[int]。
        heap: list[int] = []

        # 遍历当前序列，逐步推进状态。
        for x in nums:
            # 判断条件是否成立，选择对应处理分支。
            if len(heap) < k:
                # 调用函数/方法，推进当前步骤。
                heapq.heappush(heap, x)
            # 当前置条件不满足时，继续判断该分支条件。
            elif x > heap[0]:
                # 调用函数/方法，推进当前步骤。
                heapq.heapreplace(heap, x)

        # 返回当前函数结果。
        return heap[0]


# 定义 SolutionSort 类，封装该题解法。
class SolutionSort:
    """解法三：排序，时间 O(n log n)，代码最短、最稳定。"""

    # 定义 findKthLargest 函数/方法。
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 返回当前函数结果。
        return sorted(nums)[-k]


# 定义 SolutionCounting 类，封装该题解法。
class SolutionCounting:
    """解法四：计数（桶）法，时间 O(n + range)。

    # 执行当前语句，更新算法状态。
    当数值范围不大时很好用。这里使用动态范围 [min(nums), max(nums)]，
    # 执行当前语句，更新算法状态。
    不依赖题目给出的固定边界。
    """

    # 定义 findKthLargest 函数/方法。
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 初始化或更新变量 lo, hi。
        lo, hi = min(nums), max(nums)
        # 初始化或更新变量 count。
        count = [0] * (hi - lo + 1)

        # 遍历当前序列，逐步推进状态。
        for x in nums:
            # 更新变量 count[x - lo]，推进当前状态。
            count[x - lo] += 1

        # 初始化或更新变量 rest。
        rest = k
        # 遍历当前序列，逐步推进状态。
        for i in range(len(count) - 1, -1, -1):
            # 更新变量 rest，推进当前状态。
            rest -= count[i]
            # 判断条件是否成立，选择对应处理分支。
            if rest <= 0:
                # 返回当前函数结果。
                return i + lo

        # 主动抛出异常，提示输入或状态不合法。
        raise ValueError("invalid input")
