from __future__ import annotations

from typing import List


def heap_sort(nums: List[int], reverse: bool = False) -> List[int]:
    """堆排序（完全非递归，返回新列表，不修改原数组）。

    Args:
        nums: 待排序数组
        reverse: False 为升序，True 为降序
    """

    arr = nums[:]
    n = len(arr)
    if n <= 1:
        return arr

    _build_heap(arr, reverse)

    # 每次把堆顶（当前最大/最小）放到区间末尾，再缩小堆区间
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        _sift_down(arr, 0, end, reverse)

    return arr


def heap_sort_asc(nums: List[int]) -> List[int]:
    """升序堆排序（内部使用大顶堆）。"""

    return heap_sort(nums, reverse=False)


def heap_sort_desc(nums: List[int]) -> List[int]:
    """降序堆排序（内部使用小顶堆）。"""

    return heap_sort(nums, reverse=True)


def _build_heap(arr: List[int], reverse: bool) -> None:
    """自底向上建堆。"""

    n = len(arr)
    # 最后一个非叶子节点: (n - 2) // 2
    for start in range((n - 2) // 2, -1, -1):
        _sift_down(arr, start, n, reverse)


def _sift_down(arr: List[int], start: int, size: int, reverse: bool) -> None:
    """下沉操作。

    reverse=False: 维护大顶堆（用于升序）
    reverse=True: 维护小顶堆（用于降序）
    """

    root = start

    while True:
        left = 2 * root + 1
        if left >= size:
            return

        right = left + 1
        best = root

        if _heap_should_swap(arr[best], arr[left], reverse):
            best = left
        if right < size and _heap_should_swap(arr[best], arr[right], reverse):
            best = right

        if best == root:
            return

        arr[root], arr[best] = arr[best], arr[root]
        root = best


def _heap_should_swap(parent: int, child: int, reverse: bool) -> bool:
    """是否需要让 child 上浮替换 parent。"""

    # 升序 -> 大顶堆：child > parent 时交换
    # 降序 -> 小顶堆：child < parent 时交换
    return child < parent if reverse else child > parent


if __name__ == "__main__":
    data = [5, 1, 8, 3, 2, 7, 4, 6, 3]
    print("原数组:", data)
    print("堆排升序:", heap_sort_asc(data))
    print("堆排降序:", heap_sort_desc(data))
    print("Python sorted 升序:", sorted(data))
    print("Python sorted 降序:", sorted(data, reverse=True))
    print("原数组未修改:", data)
