from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    """解法一（推荐）：双指针迭代反转。"""

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev


class SolutionHeadInsert:
    """解法二：头插法（用 dummy 持续把节点插到表头）。"""

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head

        while cur:
            nxt = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = nxt
        return dummy.next


class SolutionStack:
    """解法三：栈辅助，思路直观但额外 O(n) 空间。"""

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        stack: list[ListNode] = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        new_head = stack.pop()
        cur = new_head
        while stack:
            node = stack.pop()
            cur.next = node
            cur = node
        cur.next = None
        return new_head
