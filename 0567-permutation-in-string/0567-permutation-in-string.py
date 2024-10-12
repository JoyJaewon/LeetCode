'''
input: 2 strings
output: boolean - true if s1's permutation is in s2

Test Cases
'ab', 'eidbaooo' -> true

if len(s1) > len(s2): False
create count dictionary for s1
window length = s1 length. 
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count, s2_count = {}, {}

        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        
        if s1_count == s2_count:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1
            s2_count[s2[left]] -= 1
            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]] 
                
            if s1_count == s2_count:
                return True
            left += 1
        
        return False
        
        

        