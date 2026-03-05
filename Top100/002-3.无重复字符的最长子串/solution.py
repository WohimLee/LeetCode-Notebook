# 导入当前解法依赖的模块或类型。
from __future__ import annotations


# 定义 Solution 类，封装该题解法。
class Solution:
    """解法一（推荐）：滑动窗口 + 记录字符最近出现位置。"""

    # 定义 lengthOfLongestSubstring 函数/方法。
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 初始化或更新变量 last: dict[str, int]。
        last: dict[str, int] = {}
        # 初始化或更新变量 left。
        left = 0
        # 初始化或更新变量 ans。
        ans = 0

        # 遍历当前序列，逐步推进状态。
        for right, ch in enumerate(s):
            # 判断条件是否成立，选择对应处理分支。
            if ch in last and last[ch] >= left:
                # 初始化或更新变量 left。
                left = last[ch] + 1
            # 初始化或更新变量 last[ch]。
            last[ch] = right
            # 初始化或更新变量 ans。
            ans = max(ans, right - left + 1)
        # 返回当前函数结果。
        return ans


# 定义 SolutionSetWindow 类，封装该题解法。
class SolutionSetWindow:
    """解法二：滑动窗口 + set，窗口内始终保持无重复。"""

    # 定义 lengthOfLongestSubstring 函数/方法。
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 初始化或更新变量 seen: set[str]。
        seen: set[str] = set()
        # 初始化或更新变量 left。
        left = 0
        # 初始化或更新变量 ans。
        ans = 0

        # 遍历当前序列，逐步推进状态。
        for right, ch in enumerate(s):
            # 当条件成立时循环处理，直到状态收敛。
            while ch in seen:
                # 调用函数/方法，推进当前步骤。
                seen.remove(s[left])
                # 更新变量 left，推进当前状态。
                left += 1
            # 调用函数/方法，推进当前步骤。
            seen.add(ch)
            # 初始化或更新变量 ans。
            ans = max(ans, right - left + 1)
        # 返回当前函数结果。
        return ans
