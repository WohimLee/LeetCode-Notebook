from __future__ import annotations

from collections import deque
from typing import List


class Solution:
    """DP：dp[i] 表示 s[:i] 是否可拆分。"""

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_len = max((len(w) for w in word_set), default=0)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            start = max(0, i - max_len)
            for j in range(start, i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]


class SolutionBFS:
    """BFS：把下标看成节点，能跳到下一个可匹配单词结束位置。"""

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_len = max((len(w) for w in word_set), default=0)
        n = len(s)
        q = deque([0])
        visited = {0}

        while q:
            start = q.popleft()
            end_limit = min(n, start + max_len)
            for end in range(start + 1, end_limit + 1):
                if s[start:end] not in word_set:
                    continue
                if end == n:
                    return True
                if end not in visited:
                    visited.add(end)
                    q.append(end)
        return False

