from __future__ import annotations

from collections import OrderedDict
from typing import Optional

class _Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev: Optional[_Node] = None
        self.next: Optional[_Node] = None

class LRUCache:
    """手写双向链表 + 哈希表，便于理解 LRU 本质。"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: dict[int, _Node] = {}
        self.head = _Node(-1, -1)  # dummy head（最久未使用在 head.next）
        self.tail = _Node(-1, -1)  # dummy tail（最近使用在 tail.prev）
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1
        # 命中后要刷新到“最近使用”位置。
        self._move_to_tail(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._move_to_tail(node)
            return

        node = _Node(key, value)
        self.map[key] = node
        self._append_to_tail(node)

        if len(self.map) > self.capacity:
            # 超出容量时，淘汰链表头部那个“最久未使用”的节点。
            oldest = self.head.next
            self._remove(oldest)
            del self.map[oldest.key]

    def _append_to_tail(self, node: _Node) -> None:
        # 尾部始终代表最近使用。
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node: _Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_tail(self, node: _Node) -> None:
        self._remove(node)
        self._append_to_tail(node)

class LRUCacheOrderedDict:
    """Python 工程化写法：OrderedDict。"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            # OrderedDict 的最左侧就是最久未使用的键。
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
