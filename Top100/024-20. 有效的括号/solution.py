# 导入当前解法依赖的模块或类型。
from __future__ import annotations


# 定义 Solution 类，封装该题解法。
class Solution:
    """栈：遇到右括号时检查与栈顶是否匹配。"""

    # 定义 isValid 函数/方法。
    def isValid(self, s: str) -> bool:
        # 初始化或更新变量 pairs。
        pairs = {')': '(', ']': '[', '}': '{'}
        # 初始化或更新变量 stack: list[str]。
        stack: list[str] = []
        # 遍历当前序列，逐步推进状态。
        for ch in s:
            # 判断条件是否成立，选择对应处理分支。
            if ch in '([{':
                # 向容器末尾追加元素，扩展结果集合。
                stack.append(ch)
            # 执行上述条件均不满足时的兜底逻辑。
            else:
                # 判断条件是否成立，选择对应处理分支。
                if not stack or stack[-1] != pairs[ch]:
                    # 返回当前函数结果。
                    return False
                # 弹出元素用于回退或继续计算。
                stack.pop()
        # 返回当前函数结果。
        return not stack


# 定义 SolutionPushExpected 类，封装该题解法。
class SolutionPushExpected:
    """入栈时直接压入“期望的右括号”，代码更紧凑。"""

    # 定义 isValid 函数/方法。
    def isValid(self, s: str) -> bool:
        # 初始化或更新变量 expect。
        expect = {'(': ')', '[': ']', '{': '}'}
        # 初始化或更新变量 stack: list[str]。
        stack: list[str] = []
        # 遍历当前序列，逐步推进状态。
        for ch in s:
            # 判断条件是否成立，选择对应处理分支。
            if ch in expect:
                # 向容器末尾追加元素，扩展结果集合。
                stack.append(expect[ch])
            # 当前置条件不满足时，继续判断该分支条件。
            elif not stack or stack.pop() != ch:
                # 返回当前函数结果。
                return False
        # 返回当前函数结果。
        return not stack


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()[]{}"))
