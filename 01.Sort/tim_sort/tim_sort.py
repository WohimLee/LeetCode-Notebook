from __future__ import annotations

from typing import List, Tuple


MIN_MERGE = 32


def tim_sort(nums: List[int], reverse: bool = False) -> List[int]:
    """教学版 TimSort（非递归）。

    特性：
    - 检测自然有序 run
    - 短 run 用二分插入排序补齐到 min_run
    - 用 run 栈按 TimSort 风格规则合并

    说明：
    - 这是便于学习的实现，未包含 CPython TimSort 的 galloping 优化
    - 返回新列表，不修改原数组
    """

    arr = nums[:]
    n = len(arr)
    if n < 2:
        return arr

    min_run = _min_run_length(n)
    runs: List[Tuple[int, int]] = []

    i = 0
    while i < n:
        run_len = _count_run_and_make_ascending(arr, i, n, reverse)

        # 短 run 扩展到 min_run，可显著减少后续 merge 次数
        if run_len < min_run:
            force = min(min_run, n - i)
            _binary_insertion_sort(arr, i, i + force, i + run_len, reverse)
            run_len = force

        runs.append((i, run_len))
        _merge_collapse(arr, runs, reverse)
        i += run_len

    _merge_force_collapse(arr, runs, reverse)
    return arr


def tim_sort_asc(nums: List[int]) -> List[int]:
    """升序 TimSort。"""

    return tim_sort(nums, reverse=False)


def tim_sort_desc(nums: List[int]) -> List[int]:
    """降序 TimSort。"""

    return tim_sort(nums, reverse=True)


def _min_run_length(n: int) -> int:
    """返回 TimSort 的 min_run（范围大致在 [32, 64]）。"""

    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def _before(a: int, b: int, reverse: bool) -> bool:
    """a 是否应该排在 b 前面。"""

    return a > b if reverse else a < b


def _count_run_and_make_ascending(arr: List[int], lo: int, hi: int, reverse: bool) -> int:
    """识别从 lo 开始的自然 run，并调整成“按目标方向有序”。"""

    run_hi = lo + 1
    if run_hi == hi:
        return 1

    # 若 next 应该排在 prev 前面，则这是“逆着目标方向”的 run，后续翻转它
    if _before(arr[run_hi], arr[lo], reverse):
        run_hi += 1
        while run_hi < hi and _before(arr[run_hi], arr[run_hi - 1], reverse):
            run_hi += 1
        arr[lo:run_hi] = reversed(arr[lo:run_hi])
    else:
        # 已经按目标方向非递减（含相等）
        run_hi += 1
        while run_hi < hi and not _before(arr[run_hi], arr[run_hi - 1], reverse):
            run_hi += 1

    return run_hi - lo


def _binary_insertion_sort(
    arr: List[int],
    lo: int,
    hi: int,
    start: int,
    reverse: bool,
) -> None:
    """对 arr[lo:hi] 做二分插入排序，假设 arr[lo:start] 已有序。"""

    if start <= lo:
        start = lo + 1

    for i in range(start, hi):
        pivot = arr[i]

        left, right = lo, i
        while left < right:
            mid = (left + right) // 2
            # 稳定性：相等时让 pivot 插在右边（bisect_right 风格）
            if _before(pivot, arr[mid], reverse):
                right = mid
            else:
                left = mid + 1

        # 把 [left, i) 整段右移一格
        arr[left + 1 : i + 1] = arr[left:i]
        arr[left] = pivot


def _merge_collapse(arr: List[int], runs: List[Tuple[int, int]], reverse: bool) -> None:
    """按 TimSort 风格栈不变量做合并。"""

    while len(runs) > 1:
        n = len(runs)

        if n >= 3 and runs[n - 3][1] <= runs[n - 2][1] + runs[n - 1][1]:
            if runs[n - 3][1] < runs[n - 1][1]:
                _merge_at(arr, runs, n - 3, reverse)
            else:
                _merge_at(arr, runs, n - 2, reverse)
        elif runs[n - 2][1] <= runs[n - 1][1]:
            _merge_at(arr, runs, n - 2, reverse)
        else:
            break


def _merge_force_collapse(arr: List[int], runs: List[Tuple[int, int]], reverse: bool) -> None:
    """收尾阶段把 run 栈完全合并。"""

    while len(runs) > 1:
        n = len(runs)
        if n >= 3 and runs[n - 3][1] < runs[n - 1][1]:
            _merge_at(arr, runs, n - 3, reverse)
        else:
            _merge_at(arr, runs, n - 2, reverse)


def _merge_at(arr: List[int], runs: List[Tuple[int, int]], i: int, reverse: bool) -> None:
    """合并 runs[i] 与 runs[i+1]。"""

    base1, len1 = runs[i]
    base2, len2 = runs[i + 1]
    assert base1 + len1 == base2

    _merge(arr, base1, base2, base2 + len2, reverse)
    runs[i] = (base1, len1 + len2)
    del runs[i + 1]


def _merge(arr: List[int], lo: int, mid: int, hi: int, reverse: bool) -> None:
    """稳定合并两个有序段 arr[lo:mid] 和 arr[mid:hi]。"""

    # 已经有序则直接返回
    if not _before(arr[mid], arr[mid - 1], reverse):
        return

    left = arr[lo:mid]
    right = arr[mid:hi]

    i = j = 0
    k = lo

    while i < len(left) and j < len(right):
        # 稳定性：相等时优先 left
        if _before(right[j], left[i], reverse):
            arr[k] = right[j]
            j += 1
        else:
            arr[k] = left[i]
            i += 1
        k += 1

    if i < len(left):
        arr[k:hi] = left[i:]
    else:
        arr[k:hi] = right[j:]


if __name__ == "__main__":
    data = [5, 1, 8, 3, 2, 7, 4, 6, 3, 9, 0, 2]
    print("原数组:", data)
    print("TimSort 升序:", tim_sort_asc(data))
    print("TimSort 降序:", tim_sort_desc(data))
    print("Python sorted 升序:", sorted(data))
    print("Python sorted 降序:", sorted(data, reverse=True))
    print("原数组未修改:", data)
