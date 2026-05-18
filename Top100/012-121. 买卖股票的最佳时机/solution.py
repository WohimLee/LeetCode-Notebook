from __future__ import annotations

from typing import List

class Solution:
    """一次遍历：维护历史最低价和当前最大利润。"""

    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best = 0
        for p in prices:
            # 一边维护历史最低价，一边尝试把今天当作卖出日。
            if p < min_price:
                min_price = p
            else:
                best = max(best, p - min_price)
        return best

class SolutionDP:
    """状态机 DP（持有/不持有），便于迁移到股票系列题。"""

    def maxProfit(self, prices: List[int]) -> int:
        hold = float('-inf')
        cash = 0
        for p in prices:
            # hold: 扫描到今天为止，手里持有一股时的最大收益。
            # cash: 扫描到今天为止，手里不持股时的最大收益。
            hold = max(hold, -p)
            cash = max(cash, hold + p)
        return cash

if __name__ == "__main__":
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices))
