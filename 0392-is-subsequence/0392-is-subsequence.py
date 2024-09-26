'''
input: 2 string - s and t
output: boolean - return true if s ia s subsequence of t

Clarifications
- s and t can be empty string
- if length of the s is greater than t, return False
- if s is empty, return True

Test Cases
'abc', 'aebece' -> True 
'aaa', 'abc' -> False
'', 'abc' -> True
'abcdef', 'abc' -> False

Approach 1) Brute Force - double for loop O(N^2)
Approach 2) 
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s) > len(t):
            return False

        j = 0
        for i in range(len(t)):
            if j < len(s) and t[i] == s[j]:
                j += 1
        
        return j == len(s) 

        