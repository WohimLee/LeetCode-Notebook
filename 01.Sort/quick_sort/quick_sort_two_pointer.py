from __future__ import annotations

from typing import List, Tuple


def quick_sort_two_pointer(nums: List[int], reverse: bool = False) -> List[int]:
    """快速排序（双指针分区 + 非递归，返回新列表，不修改原列表）。"""

    arr = nums[:]
    if len(arr) <= 1:
        return arr

    stack: List[Tuple[int, int]] = [(0, len(arr) - 1)]

    while stack:
        left, right = stack.pop()
        if left >= right:
            continue

        mid = _partition_two_pointer(arr, left, right, reverse)

        left_range = (left, mid)
        right_range = (mid + 1, right)

        left_size = left_range[1] - left_range[0]
        right_size = right_range[1] - right_range[0]

        # 先压较大区间，让较小区间优先处理，降低栈峰值
        if left_size > right_size:
            stack.append(left_range)
            stack.append(right_range)
        else:
            stack.append(right_range)
            stack.append(left_range)

    return arr


def quick_sort_two_pointer_asc(nums: List[int]) -> List[int]:
    """升序快排（双指针 + 非递归）。"""

    return quick_sort_two_pointer(nums, reverse=False)


def quick_sort_two_pointer_desc(nums: List[int]) -> List[int]:
    """降序快排（双指针 + 非递归）。"""

    return quick_sort_two_pointer(nums, reverse=True)


def _partition_two_pointer(arr: List[int], left: int, right: int, reverse: bool) -> int:
    """Hoare 双指针分区，返回左区间的右边界。"""

    pivot = arr[(left + right) // 2]
    i, j = left - 1, right + 1

    while True:
        i += 1
        while _before(arr[i], pivot, reverse):
            i += 1

        j -= 1
        while _before(pivot, arr[j], reverse):
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def _before(a: int, b: int, reverse: bool) -> bool:
    return a > b if reverse else a < b


if __name__ == "__main__":
    data = [5, 1, 8, 3, 2, 7, 4, 6, 3]
    print("原数组:", data)
    print("双指针非递归升序:", quick_sort_two_pointer_asc(data))
    print("双指针非递归降序:", quick_sort_two_pointer_desc(data))
    print("原数组未修改:", data)
