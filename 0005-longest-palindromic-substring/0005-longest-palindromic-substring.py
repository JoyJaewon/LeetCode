'''
babad -> bab

acded -> ded

a -> a
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checker(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1: right]

        result = ""
        for i in range(len(s)):
            odd_res = checker(i, i)
            even_res = checker(i, i + 1)
            result = max(result, odd_res, even_res, key=len)
        
        return result
