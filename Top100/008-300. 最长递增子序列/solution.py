# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from bisect import bisect_left
# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """解法一（推荐）：贪心 + 二分（牌堆法），时间 O(n log n)。"""

    # 定义 lengthOfLIS 函数/方法。
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 初始化或更新变量 tails: list[int]。
        tails: list[int] = []

        # 遍历当前序列，逐步推进状态。
        for x in nums:
            # 初始化或更新变量 i。
            i = bisect_left(tails, x)
            # 判断条件是否成立，选择对应处理分支。
            if i == len(tails):
                # 向容器末尾追加元素，扩展结果集合。
                tails.append(x)
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 初始化或更新变量 tails[i]。
                tails[i] = x
        # 返回当前函数结果。
        return len(tails)


# 定义 SolutionDP 类，封装该题解法。
class SolutionDP:
    """解法二：经典 DP，dp[i] 表示以 i 结尾的 LIS 长度。"""

    # 定义 lengthOfLIS 函数/方法。
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 初始化或更新变量 n。
        n = len(nums)
        # 判断条件是否成立，选择对应处理分支。
        if n == 0:
            # 返回当前函数结果。
            return 0

        # 初始化或更新变量 dp。
        dp = [1] * n
        # 初始化或更新变量 ans。
        ans = 1
        # 遍历当前序列，逐步推进状态。
        for i in range(n):
            # 遍历当前序列，逐步推进状态。
            for j in range(i):
                # 判断条件是否成立，选择对应处理分支。
                if nums[j] < nums[i]:
                    # 初始化或更新变量 dp[i]。
                    dp[i] = max(dp[i], dp[j] + 1)
            # 初始化或更新变量 ans。
            ans = max(ans, dp[i])
        # 返回当前函数结果。
        return ans


if __name__ == "__main__":
    solution = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(solution.lengthOfLIS(nums))
