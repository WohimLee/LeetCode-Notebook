# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """显式栈模拟 DFS（非递归回溯）。"""

    # 定义 combinationSum 函数/方法。
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 对数据排序，为后续有序处理做准备。
        candidates.sort()
        # 初始化或更新变量 ans: List[List[int]]。
        ans: List[List[int]] = []
        # 初始化或更新关键状态变量。
        stack: list[tuple[int, int, List[int]]] = [(0, target, [])]

        # 当条件成立时循环处理，直到状态收敛。
        while stack:
            # 弹出元素用于回退或继续计算。
            start, remain, path = stack.pop()
            # 判断条件是否成立，选择对应处理分支。
            if remain == 0:
                # 向容器末尾追加元素，扩展结果集合。
                ans.append(path)
                # 跳过本轮剩余逻辑，进入下一轮循环。
                continue

            # 遍历当前序列，逐步推进状态。
            for i in range(len(candidates) - 1, start - 1, -1):
                # 初始化或更新变量 c。
                c = candidates[i]
                # 判断条件是否成立，选择对应处理分支。
                if c > remain:
                    # 跳过本轮剩余逻辑，进入下一轮循环。
                    continue
                # 向容器末尾追加元素，扩展结果集合。
                stack.append((i, remain - c, path + [c]))
        # 返回当前函数结果。
        return ans


# 定义 SolutionDP 类，封装该题解法。
class SolutionDP:
    """完全背包式组合构造：按候选数外层循环避免重复顺序。"""

    # 定义 combinationSum 函数/方法。
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 对数据排序，为后续有序处理做准备。
        candidates.sort()
        # 初始化或更新变量 dp: list[list[list[int]]]。
        dp: list[list[list[int]]] = [[] for _ in range(target + 1)]
        # 初始化或更新变量 dp[0]。
        dp[0] = [[]]

        # 遍历当前序列，逐步推进状态。
        for c in candidates:
            # 遍历当前序列，逐步推进状态。
            for s in range(c, target + 1):
                # 遍历当前序列，逐步推进状态。
                for prev in dp[s - c]:
                    # 向容器末尾追加元素，扩展结果集合。
                    dp[s].append(prev + [c])
        # 返回当前函数结果。
        return dp[target]


if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))
