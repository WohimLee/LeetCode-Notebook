from __future__ import annotations

from typing import List


class Solution:
    """显式栈模拟 DFS（非递归回溯）。"""

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans: List[List[int]] = []
        stack: list[tuple[int, int, List[int]]] = [(0, target, [])]

        while stack:
            start, remain, path = stack.pop()
            if remain == 0:
                ans.append(path)
                continue

            for i in range(len(candidates) - 1, start - 1, -1):
                c = candidates[i]
                if c > remain:
                    continue
                stack.append((i, remain - c, path + [c]))
        return ans


class SolutionDP:
    """完全背包式组合构造：按候选数外层循环避免重复顺序。"""

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp: list[list[list[int]]] = [[] for _ in range(target + 1)]
        dp[0] = [[]]

        for c in candidates:
            for s in range(c, target + 1):
                for prev in dp[s - c]:
                    dp[s].append(prev + [c])
        return dp[target]

