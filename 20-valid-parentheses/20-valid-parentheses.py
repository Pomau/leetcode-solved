class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # Map of closing bracket to corresponding open bracket
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in bracket_map.values():
                # Push open bracket onto stack
                stack.append(c)
            elif c in bracket_map.keys():
                # Check that closing bracket matches the most recently
                # pushed open bracket
                if not stack or bracket_map[c] != stack.pop():
                    return False

        # Return True if the stack is empty, False otherwise
        return not stack