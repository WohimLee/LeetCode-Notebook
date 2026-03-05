# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
import heapq
# 导入当前解法依赖的模块或类型。
from typing import List, Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    """最小堆：每次取出 k 个链表当前头结点中的最小值。"""

    # 定义 mergeKLists 函数/方法。
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 初始化或更新关键状态变量。
        heap: list[tuple[int, int, ListNode]] = []
        # 初始化或更新变量 uid。
        uid = 0
        # 遍历当前序列，逐步推进状态。
        for node in lists:
            # 判断条件是否成立，选择对应处理分支。
            if node:
                # 调用函数/方法，推进当前步骤。
                heapq.heappush(heap, (node.val, uid, node))
                # 更新变量 uid，推进当前状态。
                uid += 1

        # 初始化或更新变量 dummy。
        dummy = ListNode(0)
        # 初始化或更新变量 tail。
        tail = dummy
        # 当条件成立时循环处理，直到状态收敛。
        while heap:
            # 初始化或更新变量 _, _, node。
            _, _, node = heapq.heappop(heap)
            # 初始化或更新变量 tail.next。
            tail.next = node
            # 初始化或更新变量 tail。
            tail = tail.next
            # 判断条件是否成立，选择对应处理分支。
            if node.next:
                # 调用函数/方法，推进当前步骤。
                heapq.heappush(heap, (node.next.val, uid, node.next))
                # 更新变量 uid，推进当前状态。
                uid += 1

        # 初始化或更新变量 tail.next。
        tail.next = None
        # 返回当前函数结果。
        return dummy.next


# 定义 SolutionPairwise 类，封装该题解法。
class SolutionPairwise:
    """两两合并（迭代版分治），不使用递归。"""

    # 定义 mergeKLists 函数/方法。
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 判断条件是否成立，选择对应处理分支。
        if not lists:
            # 返回当前函数结果。
            return None

        # 初始化或更新变量 interval。
        interval = 1
        # 初始化或更新变量 n。
        n = len(lists)
        # 当条件成立时循环处理，直到状态收敛。
        while interval < n:
            # 遍历当前序列，逐步推进状态。
            for i in range(0, n - interval, interval * 2):
                # 初始化或更新变量 lists[i]。
                lists[i] = self._merge_two(lists[i], lists[i + interval])
            # 更新变量 interval，推进当前状态。
            interval <<= 1
        # 返回当前函数结果。
        return lists[0]

    # 定义 _merge_two 函数/方法。
    def _merge_two(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化或更新变量 dummy。
        dummy = ListNode(0)
        # 初始化或更新变量 tail。
        tail = dummy
        # 当条件成立时循环处理，直到状态收敛。
        while a and b:
            # 判断条件是否成立，选择对应处理分支。
            if a.val <= b.val:
                # 初始化或更新变量 tail.next。
                tail.next = a
                # 初始化或更新变量 a。
                a = a.next
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 初始化或更新变量 tail.next。
                tail.next = b
                # 初始化或更新变量 b。
                b = b.next
            # 初始化或更新变量 tail。
            tail = tail.next
        # 初始化或更新变量 tail.next。
        tail.next = a or b
        # 返回当前函数结果。
        return dummy.next

