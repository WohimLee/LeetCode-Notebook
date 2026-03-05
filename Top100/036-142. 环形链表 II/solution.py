# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import Optional

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """Floyd 判圈后，从头和相遇点同步前进得到环入口。"""

    # 定义 detectCycle 函数/方法。
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化或更新变量 slow。
        slow = fast = head
        # 当条件成立时循环处理，直到状态收敛。
        while fast and fast.next:
            # 初始化或更新变量 slow。
            slow = slow.next
            # 初始化或更新变量 fast。
            fast = fast.next.next
            # 判断条件是否成立，选择对应处理分支。
            if slow is fast:
                # 终止当前循环，进入后续流程。
                break
        # 执行上述条件均不满足时的兜底逻辑。
        else:
            # 返回当前函数结果。
            return None

        # 初始化或更新变量 cur。
        cur = head
        # 当条件成立时循环处理，直到状态收敛。
        while cur is not slow:
            # 初始化或更新变量 cur。
            cur = cur.next
            # 初始化或更新变量 slow。
            slow = slow.next
        # 返回当前函数结果。
        return cur


# 定义 SolutionHashSet 类，封装该题解法。
class SolutionHashSet:
    """哈希表版本。"""

    # 定义 detectCycle 函数/方法。
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化或更新变量 seen: set[ListNode]。
        seen: set[ListNode] = set()
        # 初始化或更新变量 cur。
        cur = head
        # 当条件成立时循环处理，直到状态收敛。
        while cur:
            # 判断条件是否成立，选择对应处理分支。
            if cur in seen:
                # 返回当前函数结果。
                return cur
            # 调用函数/方法，推进当前步骤。
            seen.add(cur)
            # 初始化或更新变量 cur。
            cur = cur.next
        # 返回当前函数结果。
        return None

