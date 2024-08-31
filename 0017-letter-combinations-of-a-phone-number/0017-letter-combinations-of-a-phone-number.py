class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        pair = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6': 'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        curr, ans = [], []

        def backtrack(i):
            if i == len(digits):
                ans.append(''.join(curr))
                return
            
            for digit in pair[digits[i]]:
                curr.append(digit)
                backtrack(i + 1)
                curr.pop()

        
        backtrack(0)
        return ans
        