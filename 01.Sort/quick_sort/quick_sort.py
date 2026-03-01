from __future__ import annotations

from typing import List


def quick_sort(nums: List[int], reverse: bool = False) -> List[int]:
    """快速排序（返回新列表，不修改原列表）。

    Args:
        nums: 待排序数组
        reverse: False 为升序，True 为降序
    """

    arr = nums[:]
    if len(arr) <= 1:
        return arr

    _quick_sort_inplace(arr, 0, len(arr) - 1, reverse)
    return arr


def quick_sort_asc(nums: List[int]) -> List[int]:
    """升序快排。"""

    return quick_sort(nums, reverse=False)


def quick_sort_desc(nums: List[int]) -> List[int]:
    """降序快排。"""

    return quick_sort(nums, reverse=True)


def _quick_sort_inplace(arr: List[int], left: int, right: int, reverse: bool) -> None:
    if left >= right:
        return

    pivot_index = _partition(arr, left, right, reverse)
    _quick_sort_inplace(arr, left, pivot_index - 1, reverse)
    _quick_sort_inplace(arr, pivot_index + 1, right, reverse)


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
    print("升序:", quick_sort_asc(data))
    print("降序:", quick_sort_desc(data))
    print("原数组未修改:", data)
