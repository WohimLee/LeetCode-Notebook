# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    """双指针：fast 先走 n 步。"""

    # 定义 removeNthFromEnd 函数/方法。
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 初始化或更新变量 dummy。
        dummy = ListNode(0)
        # 初始化或更新变量 dummy.next。
        dummy.next = head
        # 初始化或更新变量 slow。
        slow = fast = dummy

        # 遍历当前序列，逐步推进状态。
        for _ in range(n):
            # 初始化或更新变量 fast。
            fast = fast.next

        # 当条件成立时循环处理，直到状态收敛。
        while fast and fast.next:
            # 初始化或更新变量 slow。
            slow = slow.next
            # 初始化或更新变量 fast。
            fast = fast.next

        # 初始化或更新变量 slow.next。
        slow.next = slow.next.next
        # 返回当前函数结果。
        return dummy.next


# 定义 SolutionStack 类，封装该题解法。
class SolutionStack:
    """栈记录所有节点，再定位倒数第 n 个。"""

    # 定义 removeNthFromEnd 函数/方法。
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 初始化或更新变量 dummy。
        dummy = ListNode(0)
        # 初始化或更新变量 dummy.next。
        dummy.next = head
        # 初始化或更新变量 stack: list[ListNode]。
        stack: list[ListNode] = []
        # 初始化或更新变量 cur。
        cur = dummy
        # 当条件成立时循环处理，直到状态收敛。
        while cur:
            # 向容器末尾追加元素，扩展结果集合。
            stack.append(cur)
            # 初始化或更新变量 cur。
            cur = cur.next

        # 遍历当前序列，逐步推进状态。
        for _ in range(n):
            # 弹出元素用于回退或继续计算。
            stack.pop()
        # 初始化或更新变量 prev。
        prev = stack[-1]
        # 初始化或更新变量 prev.next。
        prev.next = prev.next.next
        # 返回当前函数结果。
        return dummy.next

