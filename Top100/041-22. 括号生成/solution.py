from __future__ import annotations

from collections import deque
from typing import List


class Solution:
    """BFS 生成：状态为 (当前串, 左括号数, 右括号数)。"""

    def generateParenthesis(self, n: int) -> List[str]:
        ans: List[str] = []
        q = deque([('', 0, 0)])

        while q:
            cur, left, right = q.popleft()
            if len(cur) == 2 * n:
                ans.append(cur)
                continue
            if left < n:
                q.append((cur + '(', left + 1, right))
            if right < left:
                q.append((cur + ')', left, right + 1))
        return ans


class SolutionDP:
    """Catalan DP：dp[i] 由 '(' + dp[j] + ')' + dp[i-1-j] 组成。"""

    def generateParenthesis(self, n: int) -> List[str]:
        dp: list[list[str]] = [['']]
        for total in range(1, n + 1):
            cur: list[str] = []
            for left_count in range(total):
                right_count = total - 1 - left_count
                for left in dp[left_count]:
                    for right in dp[right_count]:
                        cur.append('(' + left + ')' + right)
            dp.append(cur)
        return dp[n]

