# 导入当前解法依赖的模块或类型。
from __future__ import annotations


# 定义 Solution 类，封装该题解法。
class Solution:
    """单栈：遇到 '[' 时保存 (之前字符串, 重复次数)。"""

    # 定义 decodeString 函数/方法。
    def decodeString(self, s: str) -> str:
        # 初始化或更新变量 stack: list[tuple[str, int]]。
        stack: list[tuple[str, int]] = []
        # 初始化或更新变量 cur。
        cur = []
        # 初始化或更新变量 num。
        num = 0

        # 遍历当前序列，逐步推进状态。
        for ch in s:
            # 判断条件是否成立，选择对应处理分支。
            if ch.isdigit():
                # 初始化或更新变量 num。
                num = num * 10 + int(ch)
            # 当前置条件不满足时，继续判断该分支条件。
            elif ch == '[':
                # 向容器末尾追加元素，扩展结果集合。
                stack.append((''.join(cur), num))
                # 初始化或更新变量 cur。
                cur = []
                # 初始化或更新变量 num。
                num = 0
            # 当前置条件不满足时，继续判断该分支条件。
            elif ch == ']':
                # 弹出元素用于回退或继续计算。
                prev, repeat = stack.pop()
                # 初始化或更新变量 cur。
                cur = [prev + ''.join(cur) * repeat]
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 向容器末尾追加元素，扩展结果集合。
                cur.append(ch)

        # 返回当前函数结果。
        return ''.join(cur)


# 定义 SolutionTwoStacks 类，封装该题解法。
class SolutionTwoStacks:
    """两个栈：一个存次数，一个存字符串。"""

    # 定义 decodeString 函数/方法。
    def decodeString(self, s: str) -> str:
        # 初始化或更新变量 num_stack: list[int]。
        num_stack: list[int] = []
        # 初始化或更新变量 str_stack: list[str]。
        str_stack: list[str] = []
        # 初始化或更新变量 cur。
        cur = ''
        # 初始化或更新变量 num。
        num = 0

        # 遍历当前序列，逐步推进状态。
        for ch in s:
            # 判断条件是否成立，选择对应处理分支。
            if ch.isdigit():
                # 初始化或更新变量 num。
                num = num * 10 + int(ch)
            # 当前置条件不满足时，继续判断该分支条件。
            elif ch == '[':
                # 向容器末尾追加元素，扩展结果集合。
                num_stack.append(num)
                # 向容器末尾追加元素，扩展结果集合。
                str_stack.append(cur)
                # 初始化或更新变量 num。
                num = 0
                # 初始化或更新变量 cur。
                cur = ''
            # 当前置条件不满足时，继续判断该分支条件。
            elif ch == ']':
                # 弹出元素用于回退或继续计算。
                repeat = num_stack.pop()
                # 弹出元素用于回退或继续计算。
                prev = str_stack.pop()
                # 初始化或更新变量 cur。
                cur = prev + cur * repeat
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 更新变量 cur，推进当前状态。
                cur += ch
        # 返回当前函数结果。
        return cur


if __name__ == "__main__":
    solution = Solution()
    print(solution.decodeString("3[a2[c]]"))
