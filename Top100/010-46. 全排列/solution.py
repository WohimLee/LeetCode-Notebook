# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """迭代插入法：逐个数字插入到已有排列的每个位置。"""

    # 定义 permute 函数/方法。
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res 保存“当前已经处理完前 k 个数字后”的所有排列。
        # 初始为 [[]]，表示空排列。
        res: List[List[int]] = [[]]
        # 遍历当前序列，逐步推进状态。
        for x in nums:
            # 把新数字 x 插入到每个旧排列的所有可能位置，得到下一层结果。
            nxt: List[List[int]] = []
            # 遍历当前序列，逐步推进状态。
            for perm in res:
                # 遍历当前序列，逐步推进状态。
                for i in range(len(perm) + 1):
                    # 例：perm=[1,3], x=2，可插入 i=0/1/2 三个位置。
                    nxt.append(perm[:i] + [x] + perm[i:])
            # 初始化或更新变量 res。
            res = nxt
        # 返回当前函数结果。
        return res


# 定义 SolutionNextPermutation 类，封装该题解法。
class SolutionNextPermutation:
    """按字典序不断求 next_permutation（非递归）。"""

    # 定义 next_permute 函数/方法。
    def next_permute(self, nums: List[int]) -> List[List[int]]:
        # 与 LeetCode 约定一致：空数组的全排列为 [[]]。
        if not nums:
            # 返回当前函数结果。
            return [[]]
        # 从最小字典序开始，持续求下一个排列，直到不存在。
        arr = sorted(nums)
        # 初始化或更新变量 ans。
        ans = [arr[:]]
        # 当条件成立时循环处理，直到状态收敛。
        while self._next_permutation(arr):
            # 向容器末尾追加元素，扩展结果集合。
            ans.append(arr[:])
        # 返回当前函数结果。
        return ans

    # 定义 _next_permutation 函数/方法。
    def _next_permutation(self, arr: List[int]) -> bool:
        # 1) 从右向左找第一个“上升对” arr[i] < arr[i+1]，i 即枢轴位置。
        i = len(arr) - 2
        # 当条件成立时循环处理，直到状态收敛。
        while i >= 0 and arr[i] >= arr[i + 1]:
            # 更新变量 i，推进当前状态。
            i -= 1
        # 找不到上升对，说明当前已是最大字典序（完全降序）。
        if i < 0:
            # 返回当前函数结果。
            return False

        # 2) 从右向左找第一个 > arr[i] 的元素，与枢轴交换。
        j = len(arr) - 1
        # 当条件成立时循环处理，直到状态收敛。
        while arr[j] <= arr[i]:
            # 更新变量 j，推进当前状态。
            j -= 1
        # 初始化或更新变量 arr[i], arr[j]。
        arr[i], arr[j] = arr[j], arr[i]

        # 3) 将 i 右侧后缀反转成最小升序，得到“刚好更大”的下一个排列。
        l, r = i + 1, len(arr) - 1
        # 当条件成立时循环处理，直到状态收敛。
        while l < r:
            # 初始化或更新变量 arr[l], arr[r]。
            arr[l], arr[r] = arr[r], arr[l]
            # 更新变量 l，推进当前状态。
            l += 1
            # 更新变量 r，推进当前状态。
            r -= 1
        # 返回当前函数结果。
        return True


# 定义 permute_recusive 函数/方法。
def permute_recusive(nums):
    # 经典回溯：path 记录当前路径，used 标记每个位置是否已被选过。
    res = []
    # 初始化或更新变量 path。
    path = []
    # 初始化或更新变量 used。
    used = [False] * len(nums)

    # 定义 backtrack 函数/方法。
    def backtrack():
        # 终止条件：路径长度等于原数组长度，收集一个完整排列。
        if len(path) == len(nums):
            # 向容器末尾追加元素，扩展结果集合。
            res.append(path[:])
            # 返回当前函数结果。
            return

        # 遍历当前序列，逐步推进状态。
        for i in range(len(nums)):
            # 判断条件是否成立，选择对应处理分支。
            if used[i]:
                # 跳过本轮剩余逻辑，进入下一轮循环。
                continue
            # 做选择
            used[i] = True
            # 向容器末尾追加元素，扩展结果集合。
            path.append(nums[i])

            # 进入下一层
            backtrack()

            # 撤销选择（回溯）
            path.pop()
            # 初始化或更新变量 used[i]。
            used[i] = False

    # 调用函数/方法，推进当前步骤。
    backtrack()
    # 返回当前函数结果。
    return res


# 定义 permute_stack 函数/方法。
def permute_stack(nums):
    # 使用显式栈模拟 DFS 回溯，避免递归调用栈。
    if not nums:
        # 返回当前函数结果。
        return [[]]

    # 初始化或更新变量 res。
    res = []
    # 栈中元素：(当前路径 path, 已使用标记 used)
    stack = [([], [False] * len(nums))]

    # 当条件成立时循环处理，直到状态收敛。
    while stack:
        # 弹出元素用于回退或继续计算。
        path, used = stack.pop()

        # 走到叶子节点，得到一个完整排列。
        if len(path) == len(nums):
            # 向容器末尾追加元素，扩展结果集合。
            res.append(path)
            # 跳过本轮剩余逻辑，进入下一轮循环。
            continue

        # 倒序入栈，保证弹栈时与常见递归 for i in range(n) 的遍历顺序一致。
        for i in range(len(nums) - 1, -1, -1):
            # 判断条件是否成立，选择对应处理分支。
            if used[i]:
                # 跳过本轮剩余逻辑，进入下一轮循环。
                continue
            # 初始化或更新变量 next_used。
            next_used = used[:]
            # 初始化或更新变量 next_used[i]。
            next_used[i] = True
            # 向容器末尾追加元素，扩展结果集合。
            stack.append((path + [nums[i]], next_used))

    # 返回当前函数结果。
    return res


# 判断条件是否成立，选择对应处理分支。
if __name__ == "__main__":
    # 初始化或更新变量 nums。
    nums = [1, 2, 3]
    # 初始化或更新变量 solution。
    solution = Solution()

    # 四种写法可任选其一进行测试。
    # res = solution.permute(nums)
    res = permute_recusive(nums)
    # res = permute_stack(nums)

    pass
