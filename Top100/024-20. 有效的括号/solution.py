from __future__ import annotations


class Solution:
    """栈：遇到右括号时检查与栈顶是否匹配。"""

    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack: list[str] = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return not stack


class SolutionPushExpected:
    """入栈时直接压入“期望的右括号”，代码更紧凑。"""

    def isValid(self, s: str) -> bool:
        expect = {'(': ')', '[': ']', '{': '}'}
        stack: list[str] = []
        for ch in s:
            if ch in expect:
                stack.append(expect[ch])
            elif not stack or stack.pop() != ch:
                return False
        return not stack

