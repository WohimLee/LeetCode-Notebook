from __future__ import annotations

from collections import deque
from typing import List

class Solution:
    """解法一（推荐）：BFS（非递归），访问到陆地就扩散整座岛。"""

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1":
                    continue
                # 发现一块还未访问的陆地，就开始扩散整座岛。
                ans += 1
                grid[i][j] = "0"
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                            # 访问过的陆地直接改成 0，避免重复入队。
                            grid[nx][ny] = "0"
                            q.append((nx, ny))
        return ans

class SolutionDFSIterative:
    """解法二：栈模拟 DFS（非递归）。"""

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1":
                    continue
                ans += 1
                stack = [(i, j)]
                grid[i][j] = "0"
                while stack:
                    x, y = stack.pop()
                    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                            grid[nx][ny] = "0"
                            stack.append((nx, ny))
        return ans

class SolutionUnionFind:
    """解法三：并查集。适合扩展到动态连通性问题。"""

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        parent = list(range(m * n))
        rank = [0] * (m * n)
        count = 0

        def idx(x: int, y: int) -> int:
            return x * n + y

        def find(x: int) -> int:
            while parent[x] != x:
                # 路径压缩，把节点直接挂到祖父节点上。
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            nonlocal count
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
            count -= 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # 初始时每块陆地先各算一个独立连通分量。
                    count += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1":
                    continue
                # 只向右、向下合并，避免同一条边被重复处理。
                if i + 1 < m and grid[i + 1][j] == "1":
                    union(idx(i, j), idx(i + 1, j))
                if j + 1 < n and grid[i][j + 1] == "1":
                    union(idx(i, j), idx(i, j + 1))

        return count

if __name__ == "__main__":
    solution = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(solution.numIslands(grid))
