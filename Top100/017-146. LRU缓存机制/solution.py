# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from collections import OrderedDict
# 导入当前解法依赖的模块或类型。
from typing import Optional


# 定义 _Node 类，封装该题解法。
class _Node:
    # 定义 __init__ 函数/方法。
    def __init__(self, key: int, value: int):
        # 初始化或更新变量 self.key。
        self.key = key
        # 初始化或更新变量 self.value。
        self.value = value
        # 初始化或更新变量 self.prev: Optional[_Node]。
        self.prev: Optional[_Node] = None
        # 初始化或更新变量 self.next: Optional[_Node]。
        self.next: Optional[_Node] = None


# 定义 LRUCache 类，封装该题解法。
class LRUCache:
    """手写双向链表 + 哈希表，便于理解 LRU 本质。"""

    # 定义 __init__ 函数/方法。
    def __init__(self, capacity: int):
        # 初始化或更新变量 self.capacity。
        self.capacity = capacity
        # 初始化或更新变量 self.map: dict[int, _Node]。
        self.map: dict[int, _Node] = {}
        # 初始化或更新变量 self.head。
        self.head = _Node(-1, -1)  # dummy head（最久未使用在 head.next）
        # 初始化或更新变量 self.tail。
        self.tail = _Node(-1, -1)  # dummy tail（最近使用在 tail.prev）
        # 初始化或更新变量 self.head.next。
        self.head.next = self.tail
        # 初始化或更新变量 self.tail.prev。
        self.tail.prev = self.head

    # 定义 get 函数/方法。
    def get(self, key: int) -> int:
        # 初始化或更新变量 node。
        node = self.map.get(key)
        # 判断条件是否成立，选择对应处理分支。
        if not node:
            # 返回当前函数结果。
            return -1
        # 调用函数/方法，推进当前步骤。
        self._move_to_tail(node)
        # 返回当前函数结果。
        return node.value

    # 定义 put 函数/方法。
    def put(self, key: int, value: int) -> None:
        # 判断条件是否成立，选择对应处理分支。
        if key in self.map:
            # 初始化或更新变量 node。
            node = self.map[key]
            # 初始化或更新变量 node.value。
            node.value = value
            # 调用函数/方法，推进当前步骤。
            self._move_to_tail(node)
            # 返回当前函数结果。
            return

        # 初始化或更新变量 node。
        node = _Node(key, value)
        # 初始化或更新变量 self.map[key]。
        self.map[key] = node
        # 调用函数/方法，推进当前步骤。
        self._append_to_tail(node)

        # 判断条件是否成立，选择对应处理分支。
        if len(self.map) > self.capacity:
            # 初始化或更新变量 oldest。
            oldest = self.head.next
            # 调用函数/方法，推进当前步骤。
            self._remove(oldest)
            # 删除不再需要的键或对象引用。
            del self.map[oldest.key]

    # 定义 _append_to_tail 函数/方法。
    def _append_to_tail(self, node: _Node) -> None:
        # 初始化或更新变量 prev。
        prev = self.tail.prev
        # 初始化或更新变量 prev.next。
        prev.next = node
        # 初始化或更新变量 node.prev。
        node.prev = prev
        # 初始化或更新变量 node.next。
        node.next = self.tail
        # 初始化或更新变量 self.tail.prev。
        self.tail.prev = node

    # 定义 _remove 函数/方法。
    def _remove(self, node: _Node) -> None:
        # 初始化或更新变量 node.prev.next。
        node.prev.next = node.next
        # 初始化或更新变量 node.next.prev。
        node.next.prev = node.prev

    # 定义 _move_to_tail 函数/方法。
    def _move_to_tail(self, node: _Node) -> None:
        # 调用函数/方法，推进当前步骤。
        self._remove(node)
        # 调用函数/方法，推进当前步骤。
        self._append_to_tail(node)


# 定义 LRUCacheOrderedDict 类，封装该题解法。
class LRUCacheOrderedDict:
    """Python 工程化写法：OrderedDict。"""

    # 定义 __init__ 函数/方法。
    def __init__(self, capacity: int):
        # 初始化或更新变量 self.capacity。
        self.capacity = capacity
        # 初始化或更新变量 self.data: OrderedDict[int, int]。
        self.data: OrderedDict[int, int] = OrderedDict()

    # 定义 get 函数/方法。
    def get(self, key: int) -> int:
        # 判断条件是否成立，选择对应处理分支。
        if key not in self.data:
            # 返回当前函数结果。
            return -1
        # 调用函数/方法，推进当前步骤。
        self.data.move_to_end(key)
        # 返回当前函数结果。
        return self.data[key]

    # 定义 put 函数/方法。
    def put(self, key: int, value: int) -> None:
        # 判断条件是否成立，选择对应处理分支。
        if key in self.data:
            # 调用函数/方法，推进当前步骤。
            self.data.move_to_end(key)
        # 初始化或更新变量 self.data[key]。
        self.data[key] = value
        # 判断条件是否成立，选择对应处理分支。
        if len(self.data) > self.capacity:
            # 调用函数/方法，推进当前步骤。
            self.data.popitem(last=False)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
