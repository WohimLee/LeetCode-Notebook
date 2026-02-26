from __future__ import annotations

from collections import Counter


class Solution:
    """标准滑动窗口：missing 表示还缺多少个字符。"""

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''

        need = Counter(t)
        missing = len(t)
        left = 0
        best_len = float('inf')
        best_l = 0

        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                cur_len = right - left + 1
                if cur_len < best_len:
                    best_len = cur_len
                    best_l = left

                left_ch = s[left]
                need[left_ch] += 1
                if need[left_ch] > 0:
                    missing += 1
                left += 1

        return '' if best_len == float('inf') else s[best_l : best_l + best_len]


class SolutionFiltered:
    """先过滤出 t 中出现过的字符，再滑窗。"""

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''

        need = Counter(t)
        required = len(need)
        filtered = [(i, ch) for i, ch in enumerate(s) if ch in need]

        have = Counter()
        formed = 0
        left = 0
        best = (float('inf'), 0, 0)

        for right, (idx_r, ch_r) in enumerate(filtered):
            have[ch_r] += 1
            if have[ch_r] == need[ch_r]:
                formed += 1

            while formed == required and left <= right:
                idx_l, ch_l = filtered[left]
                if idx_r - idx_l + 1 < best[0]:
                    best = (idx_r - idx_l + 1, idx_l, idx_r)

                have[ch_l] -= 1
                if have[ch_l] < need[ch_l]:
                    formed -= 1
                left += 1

        return '' if best[0] == float('inf') else s[best[1] : best[2] + 1]

