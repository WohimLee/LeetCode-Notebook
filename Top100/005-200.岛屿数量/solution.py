# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from collections import deque
# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """解法一（推荐）：BFS（非递归），访问到陆地就扩散整座岛。"""

    # 定义 numIslands 函数/方法。
    def numIslands(self, grid: List[List[str]]) -> int:
        # 判断条件是否成立，选择对应处理分支。
        if not grid or not grid[0]:
            # 返回当前函数结果。
            return 0

        # 初始化或更新变量 m, n。
        m, n = len(grid), len(grid[0])
        # 初始化或更新变量 ans。
        ans = 0

        # 遍历当前序列，逐步推进状态。
        for i in range(m):
            # 遍历当前序列，逐步推进状态。
            for j in range(n):
                # 判断条件是否成立，选择对应处理分支。
                if grid[i][j] != "1":
                    # 跳过本轮剩余逻辑，进入下一轮循环。
                    continue
                # 更新变量 ans，推进当前状态。
                ans += 1
                # 初始化或更新变量 grid[i][j]。
                grid[i][j] = "0"
                # 初始化或更新变量 q。
                q = deque([(i, j)])
                # 当条件成立时循环处理，直到状态收敛。
                while q:
                    # 从队列头部弹出元素，按 FIFO 顺序处理。
                    x, y = q.popleft()
                    # 遍历当前序列，逐步推进状态。
                    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                        # 判断条件是否成立，选择对应处理分支。
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                            # 初始化或更新变量 grid[nx][ny]。
                            grid[nx][ny] = "0"
                            # 向容器末尾追加元素，扩展结果集合。
                            q.append((nx, ny))
        # 返回当前函数结果。
        return ans


# 定义 SolutionDFSIterative 类，封装该题解法。
class SolutionDFSIterative:
    """解法二：栈模拟 DFS（非递归）。"""

    # 定义 numIslands 函数/方法。
    def numIslands(self, grid: List[List[str]]) -> int:
        # 判断条件是否成立，选择对应处理分支。
        if not grid or not grid[0]:
            # 返回当前函数结果。
            return 0

        # 初始化或更新变量 m, n。
        m, n = len(grid), len(grid[0])
        # 初始化或更新变量 ans。
        ans = 0

        # 遍历当前序列，逐步推进状态。
        for i in range(m):
            # 遍历当前序列，逐步推进状态。
            for j in range(n):
                # 判断条件是否成立，选择对应处理分支。
                if grid[i][j] != "1":
                    # 跳过本轮剩余逻辑，进入下一轮循环。
                    continue
                # 更新变量 ans，推进当前状态。
                ans += 1
                # 初始化或更新变量 stack。
                stack = [(i, j)]
                # 初始化或更新变量 grid[i][j]。
                grid[i][j] = "0"
                # 当条件成立时循环处理，直到状态收敛。
                while stack:
                    # 弹出元素用于回退或继续计算。
                    x, y = stack.pop()
                    # 遍历当前序列，逐步推进状态。
                    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                        # 判断条件是否成立，选择对应处理分支。
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                            # 初始化或更新变量 grid[nx][ny]。
                            grid[nx][ny] = "0"
                            # 向容器末尾追加元素，扩展结果集合。
                            stack.append((nx, ny))
        # 返回当前函数结果。
        return ans


# 定义 SolutionUnionFind 类，封装该题解法。
class SolutionUnionFind:
    """解法三：并查集。适合扩展到动态连通性问题。"""

    # 定义 numIslands 函数/方法。
    def numIslands(self, grid: List[List[str]]) -> int:
        # 判断条件是否成立，选择对应处理分支。
        if not grid or not grid[0]:
            # 返回当前函数结果。
            return 0

        # 初始化或更新变量 m, n。
        m, n = len(grid), len(grid[0])
        # 初始化或更新变量 parent。
        parent = list(range(m * n))
        # 初始化或更新变量 rank。
        rank = [0] * (m * n)
        # 初始化或更新变量 count。
        count = 0

        # 定义 idx 函数/方法。
        def idx(x: int, y: int) -> int:
            # 返回当前函数结果。
            return x * n + y

        # 定义 find 函数/方法。
        def find(x: int) -> int:
            # 当条件成立时循环处理，直到状态收敛。
            while parent[x] != x:
                # 初始化或更新变量 parent[x]。
                parent[x] = parent[parent[x]]
                # 初始化或更新变量 x。
                x = parent[x]
            # 返回当前函数结果。
            return x

        # 定义 union 函数/方法。
        def union(a: int, b: int) -> None:
            # 执行当前语句，更新算法状态。
            nonlocal count
            # 初始化或更新变量 ra, rb。
            ra, rb = find(a), find(b)
            # 判断条件是否成立，选择对应处理分支。
            if ra == rb:
                # 返回当前函数结果。
                return
            # 判断条件是否成立，选择对应处理分支。
            if rank[ra] < rank[rb]:
                # 初始化或更新变量 parent[ra]。
                parent[ra] = rb
            # 当前置条件不满足时，继续判断该分支条件。
            elif rank[ra] > rank[rb]:
                # 初始化或更新变量 parent[rb]。
                parent[rb] = ra
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 初始化或更新变量 parent[rb]。
                parent[rb] = ra
                # 更新变量 rank[ra]，推进当前状态。
                rank[ra] += 1
            # 更新变量 count，推进当前状态。
            count -= 1

        # 遍历当前序列，逐步推进状态。
        for i in range(m):
            # 遍历当前序列，逐步推进状态。
            for j in range(n):
                # 判断条件是否成立，选择对应处理分支。
                if grid[i][j] == "1":
                    # 更新变量 count，推进当前状态。
                    count += 1

        # 遍历当前序列，逐步推进状态。
        for i in range(m):
            # 遍历当前序列，逐步推进状态。
            for j in range(n):
                # 判断条件是否成立，选择对应处理分支。
                if grid[i][j] != "1":
                    # 跳过本轮剩余逻辑，进入下一轮循环。
                    continue
                # 判断条件是否成立，选择对应处理分支。
                if i + 1 < m and grid[i + 1][j] == "1":
                    # 调用函数/方法，推进当前步骤。
                    union(idx(i, j), idx(i + 1, j))
                # 判断条件是否成立，选择对应处理分支。
                if j + 1 < n and grid[i][j + 1] == "1":
                    # 调用函数/方法，推进当前步骤。
                    union(idx(i, j), idx(i, j + 1))

        # 返回当前函数结果。
        return count
