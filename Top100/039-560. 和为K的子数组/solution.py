# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from collections import defaultdict
# 导入当前解法依赖的模块或类型。
from typing import List


# 定义 Solution 类，封装该题解法。
class Solution:
    """前缀和 + 计数哈希表。"""

    # 定义 subarraySum 函数/方法。
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 初始化或更新变量 cnt。
        cnt = defaultdict(int)
        # 初始化或更新变量 cnt[0]。
        cnt[0] = 1
        # 初始化或更新变量 prefix。
        prefix = 0
        # 初始化或更新变量 ans。
        ans = 0
        # 遍历当前序列，逐步推进状态。
        for x in nums:
            # 更新变量 prefix，推进当前状态。
            prefix += x
            # 更新变量 ans，推进当前状态。
            ans += cnt[prefix - k]
            # 更新变量 cnt[prefix]，推进当前状态。
            cnt[prefix] += 1
        # 返回当前函数结果。
        return ans


# 定义 SolutionPrefixBrute 类，封装该题解法。
class SolutionPrefixBrute:
    """前缀和 + 双循环（易理解，O(n^2)）。"""

    # 定义 subarraySum 函数/方法。
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 初始化或更新变量 prefix。
        prefix = [0]
        # 遍历当前序列，逐步推进状态。
        for x in nums:
            # 向容器末尾追加元素，扩展结果集合。
            prefix.append(prefix[-1] + x)

        # 初始化或更新变量 ans。
        ans = 0
        # 初始化或更新变量 n。
        n = len(nums)
        # 遍历当前序列，逐步推进状态。
        for i in range(n):
            # 遍历当前序列，逐步推进状态。
            for j in range(i + 1, n + 1):
                # 判断条件是否成立，选择对应处理分支。
                if prefix[j] - prefix[i] == k:
                    # 更新变量 ans，推进当前状态。
                    ans += 1
        # 返回当前函数结果。
        return ans

