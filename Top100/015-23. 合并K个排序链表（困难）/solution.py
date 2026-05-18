from __future__ import annotations

import heapq
from typing import List, Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """最小堆：每次取出 k 个链表当前头结点中的最小值。"""

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # uid 作为并列值时的第二关键字，避免直接比较 ListNode。
        heap: list[tuple[int, int, ListNode]] = []
        uid = 0
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, uid, node))
                uid += 1

        dummy = ListNode(0)
        tail = dummy
        while heap:
            # 每次弹出的都是所有链表当前头结点中的最小值。
            _, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, uid, node.next))
                uid += 1

        tail.next = None
        return dummy.next

class SolutionPairwise:
    """两两合并（迭代版分治），不使用递归。"""

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        interval = 1
        n = len(lists)
        while interval < n:
            # 按 1, 2, 4, 8 ... 的步长两两合并，类似归并排序。
            for i in range(0, n - interval, interval * 2):
                lists[i] = self._merge_two(lists[i], lists[i + interval])
            interval <<= 1
        return lists[0]

    def _merge_two(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a or b
        return dummy.next

if __name__ == "__main__":
    if "ListNode" not in globals():
        class ListNode:
            def __init__(self, val: int = 0, next=None):
                self.val = val
                self.next = next

    def build_list(values):
        dummy = ListNode(0)
        cur = dummy
        for v in values:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    def list_to_values(head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals

    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    solution = Solution()
    merged = solution.mergeKLists(lists)
    print(list_to_values(merged))
