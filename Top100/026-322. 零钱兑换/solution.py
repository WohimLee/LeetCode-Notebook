# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from collections import deque
# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """完全背包 DP：dp[x] 为凑成金额 x 的最少硬币数。"""

    # 定义 coinChange 函数/方法。
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化或更新变量 INF。
        INF = amount + 1
        # 初始化或更新变量 dp。
        dp = [INF] * (amount + 1)
        # 初始化或更新变量 dp[0]。
        dp[0] = 0
        # 遍历当前序列，逐步推进状态。
        for coin in coins:
            # 遍历当前序列，逐步推进状态。
            for x in range(coin, amount + 1):
                # 初始化或更新变量 dp[x]。
                dp[x] = min(dp[x], dp[x - coin] + 1)
        # 返回当前函数结果。
        return -1 if dp[amount] == INF else dp[amount]


# 定义 SolutionBFS 类，封装该题解法。
class SolutionBFS:
    """BFS：把金额看成图上的节点，边为“加一枚硬币”。"""

    # 定义 coinChange 函数/方法。
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 判断条件是否成立，选择对应处理分支。
        if amount == 0:
            # 返回当前函数结果。
            return 0
        # 初始化或更新变量 coins。
        coins = sorted(set(coins))
        # 初始化或更新变量 q。
        q = deque([(0, 0)])  # (current_amount, steps)
        # 初始化或更新变量 visited。
        visited = {0}

        # 当条件成立时循环处理，直到状态收敛。
        while q:
            # 从队列头部弹出元素，按 FIFO 顺序处理。
            cur, steps = q.popleft()
            # 遍历当前序列，逐步推进状态。
            for coin in coins:
                # 初始化或更新变量 nxt。
                nxt = cur + coin
                # 判断条件是否成立，选择对应处理分支。
                if nxt == amount:
                    # 返回当前函数结果。
                    return steps + 1
                # 判断条件是否成立，选择对应处理分支。
                if nxt > amount:
                    # 终止当前循环，进入后续流程。
                    break
                # 判断条件是否成立，选择对应处理分支。
                if nxt in visited:
                    # 跳过本轮剩余逻辑，进入下一轮循环。
                    continue
                # 调用函数/方法，推进当前步骤。
                visited.add(nxt)
                # 向容器末尾追加元素，扩展结果集合。
                q.append((nxt, steps + 1))
        # 返回当前函数结果。
        return -1

