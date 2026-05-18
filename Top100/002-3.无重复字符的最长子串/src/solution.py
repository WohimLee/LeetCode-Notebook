from __future__ import annotations

from typing import List, Tuple

class Solution:
    """解法一（推荐）：滑动窗口 + 记录字符最近出现位置。"""

    def lengthOfLongestSubstring(self, s: str) -> int:
        last: dict[str, int] = {}
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                # 遇到重复字符时，把左边界直接跳到它上一次出现位置之后。
                left = last[ch] + 1
            last[ch] = right
            ans = max(ans, right - left + 1)
        return ans

    def longestSubstrings(self, s: str) -> Tuple[int, List[str]]:
        # last 记录每个字符最近一次出现的位置。
        last: dict[str, int] = {}
        # left 表示当前无重复窗口的左边界。
        left = 0
        # best_len 表示当前找到的最长无重复子串长度。
        best_len = 0
        # best_substrings 按出现顺序收集所有“内容去重后”的最长子串。
        best_substrings: List[str] = []
        # seen_best 用于对子串内容去重，避免相同内容重复加入结果。
        seen_best: set[str] = set()

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right

            # 当前窗口 s[left:right+1] 始终无重复。
            curr_len = right - left + 1
            if curr_len > best_len:
                best_len = curr_len
                substring = s[left : right + 1]
                best_substrings = [substring]
                seen_best = {substring}
            elif curr_len == best_len and best_len > 0:
                substring = s[left : right + 1]
                if substring not in seen_best:
                    best_substrings.append(substring)
                    seen_best.add(substring)

        return best_len, best_substrings

class SolutionSetWindow:
    """解法二：滑动窗口 + set，窗口内始终保持无重复。"""

    def lengthOfLongestSubstring(self, s: str) -> int:
        seen: set[str] = set()
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            while ch in seen:
                # 不断收缩左边界，直到窗口重新恢复无重复。
                seen.remove(s[left])
                left += 1
            seen.add(ch)
            ans = max(ans, right - left + 1)
        return ans

    def longestSubstrings(self, s: str) -> Tuple[int, List[str]]:
        seen: set[str] = set()
        left = 0
        best_len = 0
        best_substrings: List[str] = []
        seen_best: set[str] = set()

        for right, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[left])
                left += 1
            seen.add(ch)

            curr_len = right - left + 1
            if curr_len > best_len:
                best_len = curr_len
                substring = s[left : right + 1]
                best_substrings = [substring]
                seen_best = {substring}
            elif curr_len == best_len and best_len > 0:
                substring = s[left : right + 1]
                if substring not in seen_best:
                    best_substrings.append(substring)
                    seen_best.add(substring)

        return best_len, best_substrings

if __name__ == "__main__":
    solution = Solution()
    s = "abcabcbb"
    print(solution.lengthOfLongestSubstring(s))
    print(solution.longestSubstrings(s))
