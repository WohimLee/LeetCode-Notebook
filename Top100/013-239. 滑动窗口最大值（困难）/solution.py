# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
import heapq
# 导入当前解法依赖的模块或类型。
from collections import deque
# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """单调队列：队首永远是窗口最大值下标。"""

    # 定义 maxSlidingWindow 函数/方法。
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 初始化或更新变量 q: deque[int]。
        q: deque[int] = deque()
        # 初始化或更新变量 ans: List[int]。
        ans: List[int] = []

        # 遍历当前序列，逐步推进状态。
        for i, x in enumerate(nums):
            # 当条件成立时循环处理，直到状态收敛。
            while q and q[0] <= i - k:
                # 从队列头部弹出元素，按 FIFO 顺序处理。
                q.popleft()
            # 当条件成立时循环处理，直到状态收敛。
            while q and nums[q[-1]] <= x:
                # 弹出元素用于回退或继续计算。
                q.pop()
            # 向容器末尾追加元素，扩展结果集合。
            q.append(i)
            # 判断条件是否成立，选择对应处理分支。
            if i >= k - 1:
                # 向容器末尾追加元素，扩展结果集合。
                ans.append(nums[q[0]])
        # 返回当前函数结果。
        return ans


# 定义 SolutionHeap 类，封装该题解法。
class SolutionHeap:
    """大根堆（Python 用最小堆存负值）+ 懒删除。"""

    # 定义 maxSlidingWindow 函数/方法。
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 初始化或更新变量 heap: List[tuple[int, int]]。
        heap: List[tuple[int, int]] = []  # (-value, idx)
        # 初始化或更新变量 ans: List[int]。
        ans: List[int] = []

        # 遍历当前序列，逐步推进状态。
        for i, x in enumerate(nums):
            # 调用函数/方法，推进当前步骤。
            heapq.heappush(heap, (-x, i))
            # 判断条件是否成立，选择对应处理分支。
            if i >= k - 1:
                # 当条件成立时循环处理，直到状态收敛。
                while heap and heap[0][1] <= i - k:
                    # 调用函数/方法，推进当前步骤。
                    heapq.heappop(heap)
                # 向容器末尾追加元素，扩展结果集合。
                ans.append(-heap[0][0])
        # 返回当前函数结果。
        return ans


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(solution.maxSlidingWindow(nums, k))
