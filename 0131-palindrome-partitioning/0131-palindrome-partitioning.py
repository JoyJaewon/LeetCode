class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtrack(start, curr):
            if start == len(s):
                ans.append(curr[:])
                return
            
            for i in range(start, len(s)):
                substring = s[start:i+1]
                if self.isPalindrome(substring):
                    curr.append(substring)
                    backtrack(i + 1, curr)
                    curr.pop()
        
        backtrack(0, [])
        return ans 
    
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False           
            left += 1
            right -= 1

        return True
        