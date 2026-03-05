
from typing import List, Tuple

def partition_hoare(data: List[int], loIdx: int, hiIdx: int) -> int:
    pivotVal = data[loIdx]   # 常见实现：取区间第一个元素为 pivot
    lPointer = loIdx - 1      # i 从左边界外开始向右走
    rPointer = hiIdx + 1      # j 从右边界外开始向左走
    while True:
        # 找到左侧第一个 >= pivot 的位置
        lPointer += 1
        while data[lPointer] < pivotVal:
            lPointer += 1
        # 找到右侧第一个 <= pivot 的位置
        rPointer -= 1
        while data[rPointer] > pivotVal:
            rPointer -= 1
        # 指针交错时，j 即分割点
        if lPointer >= rPointer:
            return rPointer
        # 把左侧大元素和右侧小元素交换
        data[lPointer], data[rPointer] = data[rPointer], data[lPointer]


def quicksort_hoare_stack(data: List[int]) -> List[int]:
    n = len(data)
    # 长度 0/1 直接返回
    if n < 2:
        return data

    # 栈保存待处理区间
    stack: List[Tuple[int, int]] = [(0, n - 1)]
    while stack:
        loIdx, hiIdx = stack.pop()
        if loIdx >= hiIdx:
            continue

        # Hoare 分区返回分割点 p，子区间是 [lo, p] 和 [p+1, hi]
        p = partition_hoare(data, loIdx, hiIdx)
        left = (loIdx, p)
        right = (p + 1, hiIdx)

        # 先压较大区间，降低最坏情况下的栈深
        if (left[1] - left[0]) > (right[1] - right[0]):
            if left[0] < left[1]: stack.append(left)
            if right[0] < right[1]: stack.append(right)
        else:
            if right[0] < right[1]: stack.append(right)
            if left[0] < left[1]: stack.append(left)

    return data

if __name__ == "__main__":
    data = [5, 1, 8, 3, 2, 7, 4, 6, 3, 11, 5, 23]

    print("原数组:\t\t\t", data)
    print("快排结果:\t\t", quicksort_hoare_stack(data))
    print("Python sorted结果:\t", sorted(data))
    print("原数组已修改:\t\t", data)