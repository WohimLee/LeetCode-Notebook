from __future__ import annotations

from typing import Optional

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """快慢指针。"""

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


class SolutionHashSet:
    """哈希表记录访问过的节点。"""

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen: set[ListNode] = set()
        cur = head
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False

