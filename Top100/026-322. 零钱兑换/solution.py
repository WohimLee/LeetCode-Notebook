from __future__ import annotations

from collections import deque
from typing import List


class Solution:
    """完全背包 DP：dp[x] 为凑成金额 x 的最少硬币数。"""

    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return -1 if dp[amount] == INF else dp[amount]


class SolutionBFS:
    """BFS：把金额看成图上的节点，边为“加一枚硬币”。"""

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = sorted(set(coins))
        q = deque([(0, 0)])  # (current_amount, steps)
        visited = {0}

        while q:
            cur, steps = q.popleft()
            for coin in coins:
                nxt = cur + coin
                if nxt == amount:
                    return steps + 1
                if nxt > amount:
                    break
                if nxt in visited:
                    continue
                visited.add(nxt)
                q.append((nxt, steps + 1))
        return -1

