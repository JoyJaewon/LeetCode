class Solution:
    def romanToInt(self, s: str) -> int:
        pair = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        i = 0

        while i < len(s):
            if i < len(s) - 1 and pair[s[i]] < pair[s[i + 1]]:
                result += pair[s[i + 1]] - pair[s[i]]
                i += 2
            
            else:
                result += pair[s[i]]
                i += 1
        
        return result

        
        