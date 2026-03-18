# 导入当前解法依赖的模块或类型。
from __future__ import annotations


# 定义 Solution 类，封装该题解法。
class Solution:
    """栈 + 哨兵下标。"""

    # 定义 longestValidParentheses 函数/方法。
    def longestValidParentheses(self, s: str) -> int:
        # 初始化或更新变量 stack。
        stack = [-1]
        # 初始化或更新变量 ans。
        ans = 0
        # 遍历当前序列，逐步推进状态。
        for i, ch in enumerate(s):
            # 判断条件是否成立，选择对应处理分支。
            if ch == '(':
                # 向容器末尾追加元素，扩展结果集合。
                stack.append(i)
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 弹出元素用于回退或继续计算。
                stack.pop()
                # 判断条件是否成立，选择对应处理分支。
                if not stack:
                    # 向容器末尾追加元素，扩展结果集合。
                    stack.append(i)
                # 执行上述条件均不满足时的兜底逻辑。
                else:
                    # 初始化或更新变量 ans。
                    ans = max(ans, i - stack[-1])
        # 返回当前函数结果。
        return ans


# 定义 SolutionDP 类，封装该题解法。
class SolutionDP:
    """DP：dp[i] 表示以 i 结尾的最长有效括号长度。"""

    # 定义 longestValidParentheses 函数/方法。
    def longestValidParentheses(self, s: str) -> int:
        # 初始化或更新变量 n。
        n = len(s)
        # 初始化或更新变量 dp。
        dp = [0] * n
        # 初始化或更新变量 ans。
        ans = 0

        # 遍历当前序列，逐步推进状态。
        for i in range(1, n):
            # 判断条件是否成立，选择对应处理分支。
            if s[i] != ')':
                # 跳过本轮剩余逻辑，进入下一轮循环。
                continue
            # 判断条件是否成立，选择对应处理分支。
            if s[i - 1] == '(':
                # 执行当前语句，更新算法状态。
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 初始化或更新变量 prev。
                prev = i - dp[i - 1] - 1
                # 判断条件是否成立，选择对应处理分支。
                if prev >= 0 and s[prev] == '(':
                    # 调用函数/方法，推进当前步骤。
                    dp[i] = dp[i - 1] + 2 + (dp[prev - 1] if prev - 1 >= 0 else 0)
            # 初始化或更新变量 ans。
            ans = max(ans, dp[i])
        # 返回当前函数结果。
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestValidParentheses(")()())"))
