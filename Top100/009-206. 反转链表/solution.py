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
            # 把当前节点的 next 反过来指向前一个节点。
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
            # 每次把当前节点插到 dummy 后面，相当于不断头插。
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
            # 出栈顺序天然就是原链表的逆序。
            node = stack.pop()
            cur.next = node
            cur = node
        cur.next = None
        return new_head

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
    new_head = solution.reverseList(head)
    print(list_to_values(new_head))
