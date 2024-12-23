

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # 栈模拟递归过程
    stack = [(0, len(arr) - 1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        # 分区操作
        pivot_index = partition(arr, start, end)

        # 将分区后的左右子区间压入栈中
        stack.append((start, pivot_index - 1))  # 左区间
        stack.append((pivot_index + 1, end))    # 右区间

    return arr

def partition(arr, start, end):
    pivot = arr[end]  # 选择最后一个元素作为基准
    i = start - 1     # i指向小于基准的最后一个元素

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 交换小于等于基准的元素

    # 交换基准到正确位置
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1  # 返回基准的位置

# 测试
if __name__ == "__main__":
    array = [3, 6, 8, 10, 1, 2, 1]
    print("排序前:", array)
    quick_sort(array)
    print("排序后:", array)