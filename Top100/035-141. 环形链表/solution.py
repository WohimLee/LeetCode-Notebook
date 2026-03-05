# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import Optional

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """快慢指针。"""

    # 定义 hasCycle 函数/方法。
    def hasCycle(self, head: Optional[ListNode]) -> bool:
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
                # 返回当前函数结果。
                return True
        # 返回当前函数结果。
        return False


# 定义 SolutionHashSet 类，封装该题解法。
class SolutionHashSet:
    """哈希表记录访问过的节点。"""

    # 定义 hasCycle 函数/方法。
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 初始化或更新变量 seen: set[ListNode]。
        seen: set[ListNode] = set()
        # 初始化或更新变量 cur。
        cur = head
        # 当条件成立时循环处理，直到状态收敛。
        while cur:
            # 判断条件是否成立，选择对应处理分支。
            if cur in seen:
                # 返回当前函数结果。
                return True
            # 调用函数/方法，推进当前步骤。
            seen.add(cur)
            # 初始化或更新变量 cur。
            cur = cur.next
        # 返回当前函数结果。
        return False

