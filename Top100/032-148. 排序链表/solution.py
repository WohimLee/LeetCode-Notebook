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
                # 每轮把链表切成长度为 size 的两段，再做一次归并。
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

        # 先断开旧链，再按节点值排序并重新串接。
        nodes.sort(key=lambda node: node.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]

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

    solution = Solution()
    head = build_list([4, 2, 1, 3])
    sorted_head = solution.sortList(head)
    print(list_to_values(sorted_head))
