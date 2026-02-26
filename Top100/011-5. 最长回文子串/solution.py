from __future__ import annotations


class Solution:
    """中心扩展：以每个字符/缝隙为中心向两边扩张。"""

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        best_l = 0
        best_r = 0

        def expand(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        for c in range(n):
            l1, r1 = expand(c, c)
            if r1 - l1 > best_r - best_l:
                best_l, best_r = l1, r1

            l2, r2 = expand(c, c + 1)
            if r2 - l2 > best_r - best_l:
                best_l, best_r = l2, r2

        return s[best_l : best_r + 1]


class SolutionDP:
    """DP：dp[i][j] 表示 s[i:j+1] 是否为回文串。"""

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                if s[i] != s[j]:
                    continue
                if length <= 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and length > max_len:
                    start = i
                    max_len = length

        return s[start : start + max_len]

