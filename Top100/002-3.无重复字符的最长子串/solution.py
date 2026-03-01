from __future__ import annotations


class Solution:
    """解法一（推荐）：滑动窗口 + 记录字符最近出现位置。"""

    def lengthOfLongestSubstring(self, s: str) -> int:
        last: dict[str, int] = {}
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            ans = max(ans, right - left + 1)
        return ans


class SolutionSetWindow:
    """解法二：滑动窗口 + set，窗口内始终保持无重复。"""

    def lengthOfLongestSubstring(self, s: str) -> int:
        seen: set[str] = set()
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[left])
                left += 1
            seen.add(ch)
            ans = max(ans, right - left + 1)
        return ans
