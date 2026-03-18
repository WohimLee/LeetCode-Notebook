# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """一次遍历：维护历史最低价和当前最大利润。"""

    # 定义 maxProfit 函数/方法。
    def maxProfit(self, prices: List[int]) -> int:
        # 初始化或更新变量 min_price。
        min_price = float('inf')
        # 初始化或更新变量 best。
        best = 0
        # 遍历当前序列，逐步推进状态。
        for p in prices:
            # 判断条件是否成立，选择对应处理分支。
            if p < min_price:
                # 初始化或更新变量 min_price。
                min_price = p
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 初始化或更新变量 best。
                best = max(best, p - min_price)
        # 返回当前函数结果。
        return best


# 定义 SolutionDP 类，封装该题解法。
class SolutionDP:
    """状态机 DP（持有/不持有），便于迁移到股票系列题。"""

    # 定义 maxProfit 函数/方法。
    def maxProfit(self, prices: List[int]) -> int:
        # 初始化或更新变量 hold。
        hold = float('-inf')
        # 初始化或更新变量 cash。
        cash = 0
        # 遍历当前序列，逐步推进状态。
        for p in prices:
            # 初始化或更新变量 hold。
            hold = max(hold, -p)
            # 初始化或更新变量 cash。
            cash = max(cash, hold + p)
        # 返回当前函数结果。
        return cash


if __name__ == "__main__":
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices))
