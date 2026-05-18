from __future__ import annotations

class Solution:
    """栈 + 哨兵下标。"""

    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # 栈空后把当前位置当作新的“无效边界”。
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans

class SolutionDP:
    """DP：dp[i] 表示以 i 结尾的最长有效括号长度。"""

    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        ans = 0

        for i in range(1, n):
            if s[i] != ')':
                continue
            if s[i - 1] == '(':
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            else:
                # prev 是与当前 ')' 尝试配对的那个 '(' 位置。
                prev = i - dp[i - 1] - 1
                if prev >= 0 and s[prev] == '(':
                    dp[i] = dp[i - 1] + 2 + (dp[prev - 1] if prev - 1 >= 0 else 0)
            ans = max(ans, dp[i])
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestValidParentheses(")()())"))
