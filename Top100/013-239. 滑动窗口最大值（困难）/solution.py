from __future__ import annotations

import heapq
from collections import deque
from typing import List


class Solution:
    """单调队列：队首永远是窗口最大值下标。"""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q: deque[int] = deque()
        ans: List[int] = []

        for i, x in enumerate(nums):
            while q and q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans


class SolutionHeap:
    """大根堆（Python 用最小堆存负值）+ 懒删除。"""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap: List[tuple[int, int]] = []  # (-value, idx)
        ans: List[int] = []

        for i, x in enumerate(nums):
            heapq.heappush(heap, (-x, i))
            if i >= k - 1:
                while heap and heap[0][1] <= i - k:
                    heapq.heappop(heap)
                ans.append(-heap[0][0])
        return ans

