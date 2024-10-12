class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')':'(', '}':'{', ']':'['}
        stack = []

        for i in s:
            if i not in pair:
                stack.append(i)
            else:
                if not stack or stack.pop() != pair[i]:
                    return False

        return not stack