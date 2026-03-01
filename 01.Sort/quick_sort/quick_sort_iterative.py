from __future__ import annotations

from typing import List, Tuple


def quick_sort_iterative(nums: List[int], reverse: bool = False) -> List[int]:
    """快速排序（非递归版，返回新列表，不修改原列表）。"""

    arr = nums[:]
    if len(arr) <= 1:
        return arr

    stack: List[Tuple[int, int]] = [(0, len(arr) - 1)]

    while stack:
        left, right = stack.pop()
        if left >= right:
            continue

        pivot_index = _partition(arr, left, right, reverse)

        # 先压入较大区间，后处理较小区间，通常可降低栈峰值
        left_range = (left, pivot_index - 1)
        right_range = (pivot_index + 1, right)

        left_size = left_range[1] - left_range[0]
        right_size = right_range[1] - right_range[0]

        if left_size > right_size:
            stack.append(left_range)
            stack.append(right_range)
        else:
            stack.append(right_range)
            stack.append(left_range)

    return arr


def quick_sort_iterative_asc(nums: List[int]) -> List[int]:
    """升序快排（非递归版）。"""

    return quick_sort_iterative(nums, reverse=False)


def quick_sort_iterative_desc(nums: List[int]) -> List[int]:
    """降序快排（非递归版）。"""

    return quick_sort_iterative(nums, reverse=True)


def _partition(arr: List[int], left: int, right: int, reverse: bool) -> int:
    """Lomuto 分区。"""

    pivot = arr[right]
    store = left

    for i in range(left, right):
        if _should_before(arr[i], pivot, reverse):
            arr[store], arr[i] = arr[i], arr[store]
            store += 1

    arr[store], arr[right] = arr[right], arr[store]
    return store


def _should_before(a: int, b: int, reverse: bool) -> bool:
    return a > b if reverse else a < b


if __name__ == "__main__":
    data = [5, 1, 8, 3, 2, 7, 4, 6, 3]
    print("原数组:", data)
    print("非递归升序:", quick_sort_iterative_asc(data))
    print("非递归降序:", quick_sort_iterative_desc(data))
    print("原数组未修改:", data)
