class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = []
        curr_num = 0

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            elif ch == '[':
                # save current context
                stack.append(("".join(curr_str), curr_num))
                # reset for inner block
                curr_str = []
                curr_num = 0

            elif ch == ']':
                prev_str, k = stack.pop()
                decoded = prev_str + ("".join(curr_str) * k)
                curr_str = list(decoded)

            else:
                curr_str.append(ch)

        return "".join(curr_str)