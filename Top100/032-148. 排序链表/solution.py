from __future__ import annotations

from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    """链表自底向上归并排序（迭代版，无递归）。"""

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        dummy = ListNode(0)
        dummy.next = head
        size = 1

        while size < n:
            prev = dummy
            cur = dummy.next
            while cur:
                left = cur
                right = self._split(left, size)
                cur = self._split(right, size)
                merged_head, merged_tail = self._merge(left, right)
                prev.next = merged_head
                prev = merged_tail
            size <<= 1

        return dummy.next

    def _split(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        if not head:
            return None
        cur = head
        for _ in range(size - 1):
            if not cur.next:
                return None
            cur = cur.next
        nxt = cur.next
        cur.next = None
        return nxt

    def _merge(
        self, a: Optional[ListNode], b: Optional[ListNode]
    ) -> tuple[Optional[ListNode], Optional[ListNode]]:
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
        while tail.next:
            tail = tail.next
        return dummy.next, tail


class SolutionArraySort:
    """面试可讲的直观版本：先收集节点排序，再重新串起来。"""

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        nodes: list[ListNode] = []
        cur = head
        while cur:
            nxt = cur.next
            cur.next = None
            nodes.append(cur)
            cur = nxt

        nodes.sort(key=lambda node: node.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]

