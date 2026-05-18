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
                # 每个右括号都必须和最近一个未匹配的左括号配对。
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

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()[]{}"))
