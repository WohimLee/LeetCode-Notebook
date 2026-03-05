# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import Optional


# 定义 ListNode 类，封装该题解法。
class ListNode:
    # 定义 __init__ 函数/方法。
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        # 初始化或更新变量 self.val。
        self.val = val
        # 初始化或更新变量 self.next。
        self.next = next


# 定义 Solution 类，封装该题解法。
class Solution:
    """解法一（推荐）：双指针迭代反转。"""

    # 定义 reverseList 函数/方法。
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化或更新变量 prev。
        prev = None
        # 初始化或更新变量 cur。
        cur = head

        # 当条件成立时循环处理，直到状态收敛。
        while cur:
            # 初始化或更新变量 nxt。
            nxt = cur.next
            # 初始化或更新变量 cur.next。
            cur.next = prev
            # 初始化或更新变量 prev。
            prev = cur
            # 初始化或更新变量 cur。
            cur = nxt
        # 返回当前函数结果。
        return prev


# 定义 SolutionHeadInsert 类，封装该题解法。
class SolutionHeadInsert:
    """解法二：头插法（用 dummy 持续把节点插到表头）。"""

    # 定义 reverseList 函数/方法。
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化或更新变量 dummy。
        dummy = ListNode()
        # 初始化或更新变量 cur。
        cur = head

        # 当条件成立时循环处理，直到状态收敛。
        while cur:
            # 初始化或更新变量 nxt。
            nxt = cur.next
            # 初始化或更新变量 cur.next。
            cur.next = dummy.next
            # 初始化或更新变量 dummy.next。
            dummy.next = cur
            # 初始化或更新变量 cur。
            cur = nxt
        # 返回当前函数结果。
        return dummy.next


# 定义 SolutionStack 类，封装该题解法。
class SolutionStack:
    """解法三：栈辅助，思路直观但额外 O(n) 空间。"""

    # 定义 reverseList 函数/方法。
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 判断条件是否成立，选择对应处理分支。
        if head is None:
            # 返回当前函数结果。
            return None

        # 初始化或更新变量 stack: list[ListNode]。
        stack: list[ListNode] = []
        # 初始化或更新变量 cur。
        cur = head
        # 当条件成立时循环处理，直到状态收敛。
        while cur:
            # 向容器末尾追加元素，扩展结果集合。
            stack.append(cur)
            # 初始化或更新变量 cur。
            cur = cur.next

        # 弹出元素用于回退或继续计算。
        new_head = stack.pop()
        # 初始化或更新变量 cur。
        cur = new_head
        # 当条件成立时循环处理，直到状态收敛。
        while stack:
            # 弹出元素用于回退或继续计算。
            node = stack.pop()
            # 初始化或更新变量 cur.next。
            cur.next = node
            # 初始化或更新变量 cur。
            cur = node
        # 初始化或更新变量 cur.next。
        cur.next = None
        # 返回当前函数结果。
        return new_head
