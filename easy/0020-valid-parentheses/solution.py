class Solution:
    def isValid(self, s):
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()

    assert solution.isValid("()") is True
    assert solution.isValid("()[]{}") is True
    assert solution.isValid("(]") is False
    assert solution.isValid("([])") is True
    assert solution.isValid("([)]") is False

    print("All tests passed.")