# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    """双指针迭代合并。"""

    # 定义 mergeTwoLists 函数/方法。
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        # 初始化或更新变量 dummy。
        dummy = ListNode(0)
        # 初始化或更新变量 tail。
        tail = dummy
        # 初始化或更新变量 a, b。
        a, b = list1, list2

        # 当条件成立时循环处理，直到状态收敛。
        while a and b:
            # 判断条件是否成立，选择对应处理分支。
            if a.val <= b.val:
                # 初始化或更新变量 tail.next。
                tail.next = a
                # 初始化或更新变量 a。
                a = a.next
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 初始化或更新变量 tail.next。
                tail.next = b
                # 初始化或更新变量 b。
                b = b.next
            # 初始化或更新变量 tail。
            tail = tail.next

        # 初始化或更新变量 tail.next。
        tail.next = a or b
        # 返回当前函数结果。
        return dummy.next


# 定义 SolutionPointerSwap 类，封装该题解法。
class SolutionPointerSwap:
    """写法更简短：确保 a.val <= b.val 后接到结果链表。"""

    # 定义 mergeTwoLists 函数/方法。
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        # 初始化或更新变量 dummy。
        dummy = ListNode(0)
        # 初始化或更新变量 tail。
        tail = dummy
        # 初始化或更新变量 a, b。
        a, b = list1, list2
        # 当条件成立时循环处理，直到状态收敛。
        while a and b:
            # 判断条件是否成立，选择对应处理分支。
            if a.val > b.val:
                # 初始化或更新变量 a, b。
                a, b = b, a
            # 初始化或更新变量 tail.next。
            tail.next = a
            # 初始化或更新变量 a。
            a = a.next
            # 初始化或更新变量 tail。
            tail = tail.next
        # 初始化或更新变量 tail.next。
        tail.next = a or b
        # 返回当前函数结果。
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
