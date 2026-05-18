from __future__ import annotations

from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """双指针：fast 先走 n 步。"""

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy

        for _ in range(n):
            fast = fast.next

        # 保持 fast 比 slow 领先 n 个节点。
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next

class SolutionStack:
    """栈记录所有节点，再定位倒数第 n 个。"""

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        stack: list[ListNode] = []
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next

        for _ in range(n):
            stack.pop()
        prev = stack[-1]
        prev.next = prev.next.next
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

    solution = Solution()
    head = build_list([1, 2, 3, 4, 5])
    new_head = solution.removeNthFromEnd(head, 2)
    print(list_to_values(new_head))
