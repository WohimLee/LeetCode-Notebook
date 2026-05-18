from __future__ import annotations

from typing import List

class Solution:
    """显式栈模拟 DFS（非递归回溯）。"""

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 先排序，便于剪枝，也保证组合中的数字顺序稳定。
        candidates.sort()
        ans: List[List[int]] = []
        # 栈内状态：(下一次可选起点, 剩余目标值, 当前组合)。
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
                # 仍从 i 开始搜索，表示当前数字可以重复使用。
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

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))
