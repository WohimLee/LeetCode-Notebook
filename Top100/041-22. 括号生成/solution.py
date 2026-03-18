# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from collections import deque
# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """BFS 生成：状态为 (当前串, 左括号数, 右括号数)。"""

    # 定义 generateParenthesis 函数/方法。
    def generateParenthesis(self, n: int) -> List[str]:
        # 初始化或更新变量 ans: List[str]。
        ans: List[str] = []
        # 初始化或更新变量 q。
        q = deque([('', 0, 0)])

        # 当条件成立时循环处理，直到状态收敛。
        while q:
            # 从队列头部弹出元素，按 FIFO 顺序处理。
            cur, left, right = q.popleft()
            # 判断条件是否成立，选择对应处理分支。
            if len(cur) == 2 * n:
                # 向容器末尾追加元素，扩展结果集合。
                ans.append(cur)
                # 跳过本轮剩余逻辑，进入下一轮循环。
                continue
            # 判断条件是否成立，选择对应处理分支。
            if left < n:
                # 向容器末尾追加元素，扩展结果集合。
                q.append((cur + '(', left + 1, right))
            # 判断条件是否成立，选择对应处理分支。
            if right < left:
                # 向容器末尾追加元素，扩展结果集合。
                q.append((cur + ')', left, right + 1))
        # 返回当前函数结果。
        return ans


# 定义 SolutionDP 类，封装该题解法。
class SolutionDP:
    """Catalan DP：dp[i] 由 '(' + dp[j] + ')' + dp[i-1-j] 组成。"""

    # 定义 generateParenthesis 函数/方法。
    def generateParenthesis(self, n: int) -> List[str]:
        # 初始化或更新变量 dp: list[list[str]]。
        dp: list[list[str]] = [['']]
        # 遍历当前序列，逐步推进状态。
        for total in range(1, n + 1):
            # 初始化或更新变量 cur: list[str]。
            cur: list[str] = []
            # 遍历当前序列，逐步推进状态。
            for left_count in range(total):
                # 初始化或更新变量 right_count。
                right_count = total - 1 - left_count
                # 遍历当前序列，逐步推进状态。
                for left in dp[left_count]:
                    # 遍历当前序列，逐步推进状态。
                    for right in dp[right_count]:
                        # 向容器末尾追加元素，扩展结果集合。
                        cur.append('(' + left + ')' + right)
            # 向容器末尾追加元素，扩展结果集合。
            dp.append(cur)
        # 返回当前函数结果。
        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))
