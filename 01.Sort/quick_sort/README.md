# 快速排序（Quick Sort）思路详解

本文结合 `quick_sort.py` 的实现，详细说明快速排序的核心思想、执行流程，以及为什么它能同时支持升序和降序。

## 1. 快速排序是什么

快速排序是一种经典的 **分治（Divide and Conquer）** 排序算法。

它的核心思想很简单：

1. 先选一个数作为基准值（`pivot`）
2. 把数组划分成两部分
3. 让左边都“应该排在 pivot 前面”
4. 让右边都“应该排在 pivot 后面”
5. 再分别对左右两部分重复同样的操作

当子数组长度变成 `0` 或 `1` 时，它天然就是有序的。

## 2. 直观理解（为什么叫“快速”）

假设数组是：

```text
[5, 1, 8, 3, 2, 7, 4, 6]
```

如果我们选 `6` 作为基准（pivot），做一次划分后会变成类似：

```text
[5, 1, 3, 2, 4, 6, 8, 7]
```

这一步完成后，`6` 已经在它最终应该在的位置上了：

- 左边都比 `6` 小（升序）
- 右边都比 `6` 大

然后我们只需要继续排序：

- 左边 `[5, 1, 3, 2, 4]`
- 右边 `[8, 7]`

也就是说，快排的关键不在于“每次都排好一大段”，而在于：

- **每次都把一个元素放到最终位置**
- 并让问题规模不断缩小

## 3. 你当前实现的整体结构

`quick_sort.py` 中有 3 层接口：

### 3.1 对外接口

- `quick_sort(nums, reverse=False)`：通用入口
- `quick_sort_asc(nums)`：升序
- `quick_sort_desc(nums)`：降序

其中 `quick_sort()` 会先复制一份数组：

```python
arr = nums[:]
```

这样做的好处是：

- 不会修改原始输入（更安全）
- 调用者更容易调试和复用

### 3.2 递归排序函数

`_quick_sort_inplace(arr, left, right, reverse)`

职责：

- 对 `arr[left:right+1]` 这段区间进行排序
- 先分区，再递归处理左右子区间

终止条件：

```python
if left >= right:
    return
```

表示当前区间长度为 `0` 或 `1`，不需要再排。

### 3.3 分区函数（核心）

`_partition(arr, left, right, reverse)`

这是快速排序最关键的一步，它负责：

- 选一个基准值（当前实现选 `arr[right]`）
- 把“应该在 pivot 前面”的元素移动到左侧
- 最后把 `pivot` 放到正确位置
- 返回 pivot 的最终下标

## 4. 分区（Partition）是怎么工作的

当前实现采用的是 **Lomuto 分区方案**。

### 4.1 基本变量含义

```python
pivot = arr[right]
store = left
```

- `pivot`：基准值（取当前区间最后一个元素）
- `store`：下一个“应该放到左边”的位置

### 4.2 遍历区间

```python
for i in range(left, right):
    if _should_before(arr[i], pivot, reverse):
        arr[store], arr[i] = arr[i], arr[store]
        store += 1
```

含义：

- 从左到右扫描 `left ~ right-1`
- 如果 `arr[i]` 应该排在 `pivot` 前面：
  - 就把它交换到 `store` 位置
  - `store` 往右移动一格

遍历结束时：

- `[left, store-1]` 都是“应该在 pivot 前面”的元素
- `[store, right-1]` 都是不需要放在前面的元素

### 4.3 把 pivot 放回正确位置

```python
arr[store], arr[right] = arr[right], arr[store]
```

这一交换之后：

- `arr[store] == pivot`
- pivot 左边都满足排序方向要求
- pivot 右边都不满足“在前面”的条件，因此应在后面

最终返回 `store`，表示 pivot 的最终位置。

## 5. 升序和降序是怎么共用一套逻辑的

你这份代码的一个优点是：升序/降序没有写两套快排，只是抽象了比较规则。

关键在 `_should_before(a, b, reverse)`：

```python
return a > b if reverse else a < b
```

含义：

- 升序（`reverse=False`）时：`a < b` 才放前面
- 降序（`reverse=True`）时：`a > b` 才放前面

这样一来，`partition` 和 `quick_sort` 主逻辑完全复用，代码更优雅、也更容易维护。

## 6. 递归流程示意（以升序为例）

假设数组：

```text
[4, 1, 3, 2]
```

### 第 1 次分区（pivot = 2）

分区后可能得到：

```text
[1, 2, 3, 4]
```

此时 pivot `2` 已确定位置（下标 1）。

接下来递归处理：

- 左区间 `[1]`
- 右区间 `[3, 4]`

### 第 2 次分区（右区间，pivot = 4）

`[3, 4]` 分区后仍为 `[3, 4]`

再继续分解：

- `[3]`
- `[]`

都达到终止条件，排序完成。

## 7. 时间复杂度与空间复杂度

### 时间复杂度

- 平均情况：`O(n log n)`
- 最坏情况：`O(n^2)`

最坏情况通常发生在：

- 每次选到的 pivot 都非常偏（例如总是最大/最小）
- 数据本身接近有序，且 pivot 选择策略不够好（例如总选首元素或尾元素）

当前实现选 `arr[right]` 作为 pivot，代码简单，但在某些输入上可能退化。

### 空间复杂度

- 额外数组拷贝：`O(n)`（因为 `quick_sort()` 返回新列表）
- 递归栈平均：`O(log n)`
- 递归栈最坏：`O(n)`

如果改成“原地排序且不复制数组”，可以省掉那份 `O(n)` 拷贝空间。

## 8. 为什么快排常常很快（实践角度）

虽然理论上有最坏 `O(n^2)`，但在实际工程里快排依然常见，因为：

- 原地分区（数据局部性好）
- 常数因子通常较小
- 平均性能很好
- 实现灵活（可优化 pivot 策略）

## 9. 常见优化方向（你以后可以继续加）

### 9.1 随机选择 pivot

在分区前随机选一个元素与 `arr[right]` 交换，再执行分区。

好处：

- 降低遇到最坏情况的概率

### 9.2 三数取中（median-of-three）

从 `left`、`mid`、`right` 三个位置取中位数作为 pivot。

好处：

- 对接近有序的数据更稳

### 9.3 小区间改用插入排序

当子数组长度很小时（例如 <= 16），改用插入排序。

好处：

- 减少递归与分区开销，实际性能更好

### 9.4 三路快排（处理大量重复元素）

把数组分成：

- 小于 pivot
- 等于 pivot
- 大于 pivot

好处：

- 重复元素很多时性能更稳定

## 10. 快排实现中的常见坑

### 10.1 递归边界写错

正确边界：

```python
if left >= right:
    return
```

如果边界错了，容易死递归或漏排序。

### 10.2 分区后递归区间写错

分区返回 `pivot_index` 后应该递归：

- `left ~ pivot_index - 1`
- `pivot_index + 1 ~ right`

如果把 `pivot_index` 重复包含进去，会导致死循环。

### 10.3 升序/降序逻辑分散在多处

你当前实现通过 `_should_before()` 统一比较逻辑，这是个很好的设计，避免双份代码引入 bug。

### 10.4 忘记说明是否修改原数组

排序函数要明确约定：

- 原地排序（in-place）
- 返回新数组（non in-place）

你当前版本是“返回新数组”，这个约定清晰且友好。

## 11. 结合当前代码的调用示例

```python
from quick_sort import quick_sort_asc, quick_sort_desc, quick_sort

nums = [5, 1, 8, 3, 2]

print(quick_sort_asc(nums))         # [1, 2, 3, 5, 8]
print(quick_sort_desc(nums))        # [8, 5, 3, 2, 1]
print(quick_sort(nums, reverse=True))
print(nums)                         # 原数组不变
```

## 12. 一句话总结

快速排序的本质是：

- **通过一次分区，把一个 pivot 放到最终位置**
- **再递归处理左右子数组**

你当前这份实现已经具备了很好的可读性，并且通过 `reverse` 参数优雅地复用了升序/降序逻辑，是一个很适合学习和演示的版本。
