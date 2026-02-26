from __future__ import annotations


class Solution:
    """单栈：遇到 '[' 时保存 (之前字符串, 重复次数)。"""

    def decodeString(self, s: str) -> str:
        stack: list[tuple[str, int]] = []
        cur = []
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append((''.join(cur), num))
                cur = []
                num = 0
            elif ch == ']':
                prev, repeat = stack.pop()
                cur = [prev + ''.join(cur) * repeat]
            else:
                cur.append(ch)

        return ''.join(cur)


class SolutionTwoStacks:
    """两个栈：一个存次数，一个存字符串。"""

    def decodeString(self, s: str) -> str:
        num_stack: list[int] = []
        str_stack: list[str] = []
        cur = ''
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                num_stack.append(num)
                str_stack.append(cur)
                num = 0
                cur = ''
            elif ch == ']':
                repeat = num_stack.pop()
                prev = str_stack.pop()
                cur = prev + cur * repeat
            else:
                cur += ch
        return cur

