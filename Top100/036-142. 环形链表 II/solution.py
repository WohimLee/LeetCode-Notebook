from __future__ import annotations

from typing import Optional

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """Floyd 判圈后，从头和相遇点同步前进得到环入口。"""

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None

        cur = head
        while cur is not slow:
            cur = cur.next
            slow = slow.next
        return cur


class SolutionHashSet:
    """哈希表版本。"""

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen: set[ListNode] = set()
        cur = head
        while cur:
            if cur in seen:
                return cur
            seen.add(cur)
            cur = cur.next
        return None

