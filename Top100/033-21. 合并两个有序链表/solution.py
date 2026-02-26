from __future__ import annotations

from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    """双指针迭代合并。"""

    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        a, b = list1, list2

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


class SolutionPointerSwap:
    """写法更简短：确保 a.val <= b.val 后接到结果链表。"""

    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        a, b = list1, list2
        while a and b:
            if a.val > b.val:
                a, b = b, a
            tail.next = a
            a = a.next
            tail = tail.next
        tail.next = a or b
        return dummy.next

