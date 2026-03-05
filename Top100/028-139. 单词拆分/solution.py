# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from collections import deque
# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """DP：dp[i] 表示 s[:i] 是否可拆分。"""

    # 定义 wordBreak 函数/方法。
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 初始化或更新变量 word_set。
        word_set = set(wordDict)
        # 初始化或更新变量 max_len。
        max_len = max((len(w) for w in word_set), default=0)
        # 初始化或更新变量 n。
        n = len(s)
        # 初始化或更新变量 dp。
        dp = [False] * (n + 1)
        # 初始化或更新变量 dp[0]。
        dp[0] = True

        # 遍历当前序列，逐步推进状态。
        for i in range(1, n + 1):
            # 初始化或更新变量 start。
            start = max(0, i - max_len)
            # 遍历当前序列，逐步推进状态。
            for j in range(start, i):
                # 判断条件是否成立，选择对应处理分支。
                if dp[j] and s[j:i] in word_set:
                    # 初始化或更新变量 dp[i]。
                    dp[i] = True
                    # 终止当前循环，进入后续流程。
                    break
        # 返回当前函数结果。
        return dp[n]


# 定义 SolutionBFS 类，封装该题解法。
class SolutionBFS:
    """BFS：把下标看成节点，能跳到下一个可匹配单词结束位置。"""

    # 定义 wordBreak 函数/方法。
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 初始化或更新变量 word_set。
        word_set = set(wordDict)
        # 初始化或更新变量 max_len。
        max_len = max((len(w) for w in word_set), default=0)
        # 初始化或更新变量 n。
        n = len(s)
        # 初始化或更新变量 q。
        q = deque([0])
        # 初始化或更新变量 visited。
        visited = {0}

        # 当条件成立时循环处理，直到状态收敛。
        while q:
            # 从队列头部弹出元素，按 FIFO 顺序处理。
            start = q.popleft()
            # 初始化或更新变量 end_limit。
            end_limit = min(n, start + max_len)
            # 遍历当前序列，逐步推进状态。
            for end in range(start + 1, end_limit + 1):
                # 判断条件是否成立，选择对应处理分支。
                if s[start:end] not in word_set:
                    # 跳过本轮剩余逻辑，进入下一轮循环。
                    continue
                # 判断条件是否成立，选择对应处理分支。
                if end == n:
                    # 返回当前函数结果。
                    return True
                # 判断条件是否成立，选择对应处理分支。
                if end not in visited:
                    # 调用函数/方法，推进当前步骤。
                    visited.add(end)
                    # 向容器末尾追加元素，扩展结果集合。
                    q.append(end)
        # 返回当前函数结果。
        return False

