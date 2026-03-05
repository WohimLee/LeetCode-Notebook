# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """解法一（推荐）：排序 + 双指针，时间 O(n^2)。"""

    # 定义 threeSum 函数/方法。
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 对数据排序，为后续有序处理做准备。
        nums.sort()
        # 初始化或更新变量 n。
        n = len(nums)
        # 初始化或更新变量 ans: List[List[int]]。
        ans: List[List[int]] = []

        # 遍历当前序列，逐步推进状态。
        for i in range(n - 2):
            # 初始化或更新变量 x。
            x = nums[i]
            # 判断条件是否成立，选择对应处理分支。
            if i > 0 and x == nums[i - 1]:
                # 跳过本轮剩余逻辑，进入下一轮循环。
                continue
            # 判断条件是否成立，选择对应处理分支。
            if x > 0:
                # 终止当前循环，进入后续流程。
                break

            # 初始化或更新变量 l, r。
            l, r = i + 1, n - 1
            # 当条件成立时循环处理，直到状态收敛。
            while l < r:
                # 初始化或更新变量 s。
                s = x + nums[l] + nums[r]
                # 判断条件是否成立，选择对应处理分支。
                if s < 0:
                    # 更新变量 l，推进当前状态。
                    l += 1
                # 当前置条件不满足时，继续判断该分支条件。
                elif s > 0:
                    # 更新变量 r，推进当前状态。
                    r -= 1
                # 执行上述条件均不满足时的兜底逻辑。
                else:
                    # 向容器末尾追加元素，扩展结果集合。
                    ans.append([x, nums[l], nums[r]])
                    # 更新变量 l，推进当前状态。
                    l += 1
                    # 更新变量 r，推进当前状态。
                    r -= 1
                    # 当条件成立时循环处理，直到状态收敛。
                    while l < r and nums[l] == nums[l - 1]:
                        # 更新变量 l，推进当前状态。
                        l += 1
                    # 当条件成立时循环处理，直到状态收敛。
                    while l < r and nums[r] == nums[r + 1]:
                        # 更新变量 r，推进当前状态。
                        r -= 1
        # 返回当前函数结果。
        return ans


# 定义 SolutionHash 类，封装该题解法。
class SolutionHash:
    """解法二：固定第一个数 + 哈希去重，思路直观。"""

    # 定义 threeSum 函数/方法。
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 对数据排序，为后续有序处理做准备。
        nums.sort()
        # 初始化或更新变量 n。
        n = len(nums)
        # 初始化或更新变量 ans: List[List[int]]。
        ans: List[List[int]] = []

        # 遍历当前序列，逐步推进状态。
        for i in range(n - 2):
            # 判断条件是否成立，选择对应处理分支。
            if i > 0 and nums[i] == nums[i - 1]:
                # 跳过本轮剩余逻辑，进入下一轮循环。
                continue
            # 初始化或更新变量 target。
            target = -nums[i]
            # 初始化或更新变量 seen: set[int]。
            seen: set[int] = set()
            # 初始化或更新变量 used_second: set[int]。
            used_second: set[int] = set()

            # 遍历当前序列，逐步推进状态。
            for j in range(i + 1, n):
                # 初始化或更新变量 b。
                b = nums[j]
                # 初始化或更新变量 c。
                c = target - b
                # 判断条件是否成立，选择对应处理分支。
                if c in seen and b not in used_second:
                    # 向容器末尾追加元素，扩展结果集合。
                    ans.append([nums[i], c, b])
                    # 调用函数/方法，推进当前步骤。
                    used_second.add(b)
                # 调用函数/方法，推进当前步骤。
                seen.add(b)
        # 返回当前函数结果。
        return ans
