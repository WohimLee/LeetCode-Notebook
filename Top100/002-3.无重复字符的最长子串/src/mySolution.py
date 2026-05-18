def solution(string):
    # seen 用来维护当前窗口内出现过的字符。
    # 整个窗口始终保持“无重复字符”这个性质。
    seen = set()
    # lIdx 是滑动窗口左边界。
    lIdx = 0
    # max_len 记录目前找到的最长无重复子串长度。
    max_len = 0
    # res_str 收集所有最长子串。
    # 这里用 set，是为了对子串内容去重。
    res_str = set()

    # rIdx 是滑动窗口右边界，不断向右扩展窗口。
    for rIdx, char in enumerate(string):

        # 如果当前字符已经在窗口中，说明出现重复，
        # 需要不断移动左边界，并把移出窗口的字符从 seen 中删除，
        # 直到当前窗口重新恢复“无重复”为止。
        while char in seen:
            seen.remove(string[lIdx])
            lIdx += 1

        # 当前字符可以安全加入窗口。
        seen.add(char)

        # 现在窗口 string[lIdx:rIdx+1] 一定是不含重复字符的。
        cur_len = rIdx - lIdx + 1

        # 如果找到了更长的无重复子串，
        # 更新最大长度，并重置结果集合。
        if cur_len > max_len:
            max_len = cur_len
            sub_str = string[lIdx: rIdx + 1]
            res_str = {sub_str}
        # 如果当前窗口长度和最大长度相同，
        # 就把这个子串也加入结果中。
        elif cur_len == max_len and max_len > 0:
            sub_str = string[lIdx: rIdx + 1]
            res_str.add(sub_str)

    return max_len, res_str

if __name__ == "__main__":
    s1 = "abcabcbb"
    s2 = "ababcbcddabcdeab"
    print(solution(s2))
