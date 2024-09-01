class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  
        pair = {')':'(', '}': '{', ']': '['}

        for i in s:
            if i not in pair:
                stack.append(i)
                continue
            if not stack or stack.pop() != pair[i]:
                return False
        
        return not stack
        