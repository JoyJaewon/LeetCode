class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < n:
                prev_day = stack.pop()
                ans[prev_day] = i - prev_day
            stack.append(i)
        
        return ans