
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # 初始化为第一个字符串
    prefix = strs[0]
    
    # 遍历其他字符串
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]  # 每次去掉最后一个字符
            if not prefix:
                return ""
    return prefix


def leetcode(string_list: list[str]):

    prefix = string_list[0]
    for string in string_list[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

if __name__ == "__main__":
    # 示例测试
    print(longestCommonPrefix(["flower", "flow", "flight"]))  # 输出 "fl"
    print(longestCommonPrefix(["dog", "racecar", "car"]))     # 输出 ""
