from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        def isValid(s):
            count = 0
            for char in s:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        queue = deque([s])
        visited = set([s])
        found = False
        result = []

        while queue:
            current = queue.popleft()

            if isValid(current):
                result.append(current)
                found = True

            if found:
                continue

            for i in range(len(current)):
                if current[i] not in ('(', ')'):
                    continue
                next_state = current[:i] + current[i+1:]
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)

        return result
