# 导入当前解法依赖的模块或类型。
from __future__ import annotations

# 导入当前解法依赖的模块或类型。
from collections import Counter


# 定义 Solution 类，封装该题解法。
class Solution:
    """标准滑动窗口：missing 表示还缺多少个字符。"""

    # 定义 minWindow 函数/方法。
    def minWindow(self, s: str, t: str) -> str:
        # 判断条件是否成立，选择对应处理分支。
        if not s or not t:
            # 返回当前函数结果。
            return ''

        # 初始化或更新变量 need。
        need = Counter(t)
        # 初始化或更新变量 missing。
        missing = len(t)
        # 初始化或更新变量 left。
        left = 0
        # 初始化或更新变量 best_len。
        best_len = float('inf')
        # 初始化或更新变量 best_l。
        best_l = 0

        # 遍历当前序列，逐步推进状态。
        for right, ch in enumerate(s):
            # 判断条件是否成立，选择对应处理分支。
            if need[ch] > 0:
                # 更新变量 missing，推进当前状态。
                missing -= 1
            # 更新变量 need[ch]，推进当前状态。
            need[ch] -= 1

            # 当条件成立时循环处理，直到状态收敛。
            while missing == 0:
                # 初始化或更新变量 cur_len。
                cur_len = right - left + 1
                # 判断条件是否成立，选择对应处理分支。
                if cur_len < best_len:
                    # 初始化或更新变量 best_len。
                    best_len = cur_len
                    # 初始化或更新变量 best_l。
                    best_l = left

                # 初始化或更新变量 left_ch。
                left_ch = s[left]
                # 更新变量 need[left_ch]，推进当前状态。
                need[left_ch] += 1
                # 判断条件是否成立，选择对应处理分支。
                if need[left_ch] > 0:
                    # 更新变量 missing，推进当前状态。
                    missing += 1
                # 更新变量 left，推进当前状态。
                left += 1

        # 返回当前函数结果。
        return '' if best_len == float('inf') else s[best_l : best_l + best_len]


# 定义 SolutionFiltered 类，封装该题解法。
class SolutionFiltered:
    """先过滤出 t 中出现过的字符，再滑窗。"""

    # 定义 minWindow 函数/方法。
    def minWindow(self, s: str, t: str) -> str:
        # 判断条件是否成立，选择对应处理分支。
        if not s or not t:
            # 返回当前函数结果。
            return ''

        # 初始化或更新变量 need。
        need = Counter(t)
        # 初始化或更新变量 required。
        required = len(need)
        # 初始化或更新变量 filtered。
        filtered = [(i, ch) for i, ch in enumerate(s) if ch in need]

        # 初始化或更新变量 have。
        have = Counter()
        # 初始化或更新变量 formed。
        formed = 0
        # 初始化或更新变量 left。
        left = 0
        # 初始化或更新变量 best。
        best = (float('inf'), 0, 0)

        # 遍历当前序列，逐步推进状态。
        for right, (idx_r, ch_r) in enumerate(filtered):
            # 更新变量 have[ch_r]，推进当前状态。
            have[ch_r] += 1
            # 判断条件是否成立，选择对应处理分支。
            if have[ch_r] == need[ch_r]:
                # 更新变量 formed，推进当前状态。
                formed += 1

            # 当条件成立时循环处理，直到状态收敛。
            while formed == required and left <= right:
                # 初始化或更新变量 idx_l, ch_l。
                idx_l, ch_l = filtered[left]
                # 判断条件是否成立，选择对应处理分支。
                if idx_r - idx_l + 1 < best[0]:
                    # 初始化或更新变量 best。
                    best = (idx_r - idx_l + 1, idx_l, idx_r)

                # 更新变量 have[ch_l]，推进当前状态。
                have[ch_l] -= 1
                # 判断条件是否成立，选择对应处理分支。
                if have[ch_l] < need[ch_l]:
                    # 更新变量 formed，推进当前状态。
                    formed -= 1
                # 更新变量 left，推进当前状态。
                left += 1

        # 返回当前函数结果。
        return '' if best[0] == float('inf') else s[best[1] : best[2] + 1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"))
