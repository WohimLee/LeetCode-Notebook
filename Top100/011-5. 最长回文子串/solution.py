# 导入当前解法依赖的模块或类型。
from __future__ import annotations


# 定义 Solution 类，封装该题解法。
class Solution:
    """中心扩展：以每个字符/缝隙为中心向两边扩张。"""

    # 定义 longestPalindrome 函数/方法。
    def longestPalindrome(self, s: str) -> str:
        # 初始化或更新变量 n。
        n = len(s)
        # 判断条件是否成立，选择对应处理分支。
        if n < 2:
            # 返回当前函数结果。
            return s

        # 初始化或更新变量 best_l。
        best_l = 0
        # 初始化或更新变量 best_r。
        best_r = 0

        # 定义 expand 函数/方法。
        def expand(l: int, r: int) -> tuple[int, int]:
            # 当条件成立时循环处理，直到状态收敛。
            while l >= 0 and r < n and s[l] == s[r]:
                # 更新变量 l，推进当前状态。
                l -= 1
                # 更新变量 r，推进当前状态。
                r += 1
            # 返回当前函数结果。
            return l + 1, r - 1

        # 遍历当前序列，逐步推进状态。
        for c in range(n):
            # 初始化或更新变量 l1, r1。
            l1, r1 = expand(c, c)
            # 判断条件是否成立，选择对应处理分支。
            if r1 - l1 > best_r - best_l:
                # 初始化或更新变量 best_l, best_r。
                best_l, best_r = l1, r1

            # 初始化或更新变量 l2, r2。
            l2, r2 = expand(c, c + 1)
            # 判断条件是否成立，选择对应处理分支。
            if r2 - l2 > best_r - best_l:
                # 初始化或更新变量 best_l, best_r。
                best_l, best_r = l2, r2

        # 返回当前函数结果。
        return s[best_l : best_r + 1]


# 定义 SolutionDP 类，封装该题解法。
class SolutionDP:
    """DP：dp[i][j] 表示 s[i:j+1] 是否为回文串。"""

    # 定义 longestPalindrome 函数/方法。
    def longestPalindrome(self, s: str) -> str:
        # 初始化或更新变量 n。
        n = len(s)
        # 判断条件是否成立，选择对应处理分支。
        if n < 2:
            # 返回当前函数结果。
            return s

        # 初始化或更新变量 dp。
        dp = [[False] * n for _ in range(n)]
        # 初始化或更新变量 start。
        start = 0
        # 初始化或更新变量 max_len。
        max_len = 1

        # 遍历当前序列，逐步推进状态。
        for i in range(n):
            # 初始化或更新变量 dp[i][i]。
            dp[i][i] = True

        # 遍历当前序列，逐步推进状态。
        for length in range(2, n + 1):
            # 遍历当前序列，逐步推进状态。
            for i in range(0, n - length + 1):
                # 初始化或更新变量 j。
                j = i + length - 1
                # 判断条件是否成立，选择对应处理分支。
                if s[i] != s[j]:
                    # 跳过本轮剩余逻辑，进入下一轮循环。
                    continue
                # 判断条件是否成立，选择对应处理分支。
                if length <= 3:
                    # 初始化或更新变量 dp[i][j]。
                    dp[i][j] = True
                # 执行上述条件均不满足时的兜底逻辑。
                else:
                    # 初始化或更新变量 dp[i][j]。
                    dp[i][j] = dp[i + 1][j - 1]

                # 判断条件是否成立，选择对应处理分支。
                if dp[i][j] and length > max_len:
                    # 初始化或更新变量 start。
                    start = i
                    # 初始化或更新变量 max_len。
                    max_len = length

        # 返回当前函数结果。
        return s[start : start + max_len]

