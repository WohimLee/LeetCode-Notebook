# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from collections import deque
# 导入当前解法依赖的模块或类型。
from functools import lru_cache
# 导入当前解法依赖的模块或类型。
from typing import List


# 定义四联通方向：上、下、左、右。
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


# 定义 Solution 类，封装该题推荐解法。
class Solution:
    """解法一（推荐）：DFS + 记忆化搜索。"""

    # 定义 longestIncreasingPath 函数/方法。
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 空矩阵直接返回 0。
        if not matrix or not matrix[0]:
            # 返回当前函数结果。
            return 0

        # 初始化或更新变量 m, n。
        m, n = len(matrix), len(matrix[0])

        # 定义 dfs 函数/方法。
        @lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> int:
            # 至少包含自己这个格子，因此初始长度为 1。
            best = 1

            # 枚举四个方向，只能走向更大的邻居。
            for di, dj in DIRECTIONS:
                # 初始化或更新变量 ni, nj。
                ni, nj = i + di, j + dj

                # 越界则跳过。
                if not (0 <= ni < m and 0 <= nj < n):
                    # 跳过本轮剩余逻辑，进入下一轮循环。
                    continue

                # 只有严格递增时才能继续走。
                if matrix[ni][nj] > matrix[i][j]:
                    # 选择当前邻居后，路径长度为 1 + 从邻居出发的最优值。
                    best = max(best, 1 + dfs(ni, nj))

            # 返回“从 (i, j) 出发”的最长递增路径长度。
            return best

        # 枚举每个格子作为起点，答案取最大值。
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        # 返回当前函数结果。
        return ans


# 定义 SolutionTopo 类，封装 DAG 拓扑排序解法。
class SolutionTopo:
    """解法二：拓扑排序 + 分层 BFS。"""

    # 定义 longestIncreasingPath 函数/方法。
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 空矩阵直接返回 0。
        if not matrix or not matrix[0]:
            # 返回当前函数结果。
            return 0

        # 初始化或更新变量 m, n。
        m, n = len(matrix), len(matrix[0])
        # out_degree[i][j] 表示当前格子能走向多少个“更大的邻居”。
        out_degree = [[0] * n for _ in range(m)]
        # 队列初始装入所有 out_degree == 0 的点，也就是局部峰值。
        queue = deque()

        # 预处理每个点的出度。
        for i in range(m):
            for j in range(n):
                for di, dj in DIRECTIONS:
                    # 初始化或更新变量 ni, nj。
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                        out_degree[i][j] += 1

                # 没有更大的邻居，说明它是某条递增路径的终点。
                if out_degree[i][j] == 0:
                    queue.append((i, j))

        # 分层 BFS 的层数，就是最长递增路径长度。
        layers = 0

        while queue:
            layers += 1

            # 一次处理当前层的所有节点。
            for _ in range(len(queue)):
                # 弹出当前层节点。
                i, j = queue.popleft()

                # 反向找“更小的邻居”，因为这些点可以走到当前点。
                for di, dj in DIRECTIONS:
                    # 初始化或更新变量 ni, nj。
                    ni, nj = i + di, j + dj

                    if not (0 <= ni < m and 0 <= nj < n):
                        continue

                    # 只有更小的邻居，才会把当前点当成它的后继。
                    if matrix[ni][nj] < matrix[i][j]:
                        out_degree[ni][nj] -= 1

                        # 当它所有“更大后继”都被剥掉后，进入下一层。
                        if out_degree[ni][nj] == 0:
                            queue.append((ni, nj))

        # 返回当前函数结果。
        return layers


# 定义 SolutionSortedDP 类，封装排序 DP 解法。
class SolutionSortedDP:
    """解法三：按数值从小到大排序，再做二维 DP。"""

    # 定义 longestIncreasingPath 函数/方法。
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 空矩阵直接返回 0。
        if not matrix or not matrix[0]:
            # 返回当前函数结果。
            return 0

        # 初始化或更新变量 m, n。
        m, n = len(matrix), len(matrix[0])
        # dp[i][j] 表示“以 (i, j) 结尾”的最长递增路径长度。
        dp = [[1] * n for _ in range(m)]

        # 把所有格子展开后按值升序排序。
        cells = sorted((matrix[i][j], i, j) for i in range(m) for j in range(n))
        # 初始化或更新变量 ans。
        ans = 1

        # 当前格子只从比它更小的相邻格子转移过来。
        for _, i, j in cells:
            for di, dj in DIRECTIONS:
                # 初始化或更新变量 ni, nj。
                ni, nj = i + di, j + dj

                if not (0 <= ni < m and 0 <= nj < n):
                    continue

                # 只有更小邻居才能接到当前格子，形成递增路径。
                if matrix[ni][nj] < matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dp[ni][nj] + 1)

            ans = max(ans, dp[i][j])

        # 返回当前函数结果。
        return ans


# 判断条件是否成立，选择对应处理分支。
if __name__ == "__main__":
    matrix1 = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    matrix2 = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    matrix3 = [[1]]

    # 三种实现都可以独立测试。
    sol1 = Solution()
    sol2 = SolutionTopo()
    sol3 = SolutionSortedDP()

    print(sol1.longestIncreasingPath(matrix1))
    print(sol2.longestIncreasingPath(matrix2))
    print(sol3.longestIncreasingPath(matrix3))
