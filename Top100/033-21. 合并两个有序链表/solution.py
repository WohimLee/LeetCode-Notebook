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
            # 每次把较小节点接到结果链表尾部。
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
            # 通过交换引用，始终让 a 指向当前较小的那个节点。
            if a.val > b.val:
                a, b = b, a
            tail.next = a
            a = a.next
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

    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    solution = Solution()
    merged = solution.mergeTwoLists(l1, l2)
    print(list_to_values(merged))
