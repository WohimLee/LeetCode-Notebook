# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    """链表自底向上归并排序（迭代版，无递归）。"""

    # 定义 sortList 函数/方法。
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 判断条件是否成立，选择对应处理分支。
        if not head or not head.next:
            # 返回当前函数结果。
            return head

        # 初始化或更新变量 n。
        n = 0
        # 初始化或更新变量 cur。
        cur = head
        # 当条件成立时循环处理，直到状态收敛。
        while cur:
            # 更新变量 n，推进当前状态。
            n += 1
            # 初始化或更新变量 cur。
            cur = cur.next

        # 初始化或更新变量 dummy。
        dummy = ListNode(0)
        # 初始化或更新变量 dummy.next。
        dummy.next = head
        # 初始化或更新变量 size。
        size = 1

        # 当条件成立时循环处理，直到状态收敛。
        while size < n:
            # 初始化或更新变量 prev。
            prev = dummy
            # 初始化或更新变量 cur。
            cur = dummy.next
            # 当条件成立时循环处理，直到状态收敛。
            while cur:
                # 初始化或更新变量 left。
                left = cur
                # 初始化或更新变量 right。
                right = self._split(left, size)
                # 初始化或更新变量 cur。
                cur = self._split(right, size)
                # 初始化或更新变量 merged_head, merged_tail。
                merged_head, merged_tail = self._merge(left, right)
                # 初始化或更新变量 prev.next。
                prev.next = merged_head
                # 初始化或更新变量 prev。
                prev = merged_tail
            # 更新变量 size，推进当前状态。
            size <<= 1

        # 返回当前函数结果。
        return dummy.next

    # 定义 _split 函数/方法。
    def _split(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        # 判断条件是否成立，选择对应处理分支。
        if not head:
            # 返回当前函数结果。
            return None
        # 初始化或更新变量 cur。
        cur = head
        # 遍历当前序列，逐步推进状态。
        for _ in range(size - 1):
            # 判断条件是否成立，选择对应处理分支。
            if not cur.next:
                # 返回当前函数结果。
                return None
            # 初始化或更新变量 cur。
            cur = cur.next
        # 初始化或更新变量 nxt。
        nxt = cur.next
        # 初始化或更新变量 cur.next。
        cur.next = None
        # 返回当前函数结果。
        return nxt

    # 定义 _merge 函数/方法。
    def _merge(
        self, a: Optional[ListNode], b: Optional[ListNode]
    ) -> tuple[Optional[ListNode], Optional[ListNode]]:
        # 初始化或更新变量 dummy。
        dummy = ListNode(0)
        # 初始化或更新变量 tail。
        tail = dummy
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
        # 当条件成立时循环处理，直到状态收敛。
        while tail.next:
            # 初始化或更新变量 tail。
            tail = tail.next
        # 返回当前函数结果。
        return dummy.next, tail


# 定义 SolutionArraySort 类，封装该题解法。
class SolutionArraySort:
    """面试可讲的直观版本：先收集节点排序，再重新串起来。"""

    # 定义 sortList 函数/方法。
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 判断条件是否成立，选择对应处理分支。
        if not head or not head.next:
            # 返回当前函数结果。
            return head

        # 初始化或更新变量 nodes: list[ListNode]。
        nodes: list[ListNode] = []
        # 初始化或更新变量 cur。
        cur = head
        # 当条件成立时循环处理，直到状态收敛。
        while cur:
            # 初始化或更新变量 nxt。
            nxt = cur.next
            # 初始化或更新变量 cur.next。
            cur.next = None
            # 向容器末尾追加元素，扩展结果集合。
            nodes.append(cur)
            # 初始化或更新变量 cur。
            cur = nxt

        # 对数据排序，为后续有序处理做准备。
        nodes.sort(key=lambda node: node.val)
        # 遍历当前序列，逐步推进状态。
        for i in range(len(nodes) - 1):
            # 初始化或更新变量 nodes[i].next。
            nodes[i].next = nodes[i + 1]
        # 返回当前函数结果。
        return nodes[0]


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
    head = build_list([4, 2, 1, 3])
    sorted_head = solution.sortList(head)
    print(list_to_values(sorted_head))
