class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filtered = [c.lower() for c in s if c.isalnum()]
        left = 0
        right = len(s_filtered) - 1

        while left < right:
            if s_filtered[left] != s_filtered[right]:
                return False
            left += 1
            right -= 1
        
        return True
        