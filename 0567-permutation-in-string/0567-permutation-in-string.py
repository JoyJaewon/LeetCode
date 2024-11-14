'''
true if s2 contains a permutation of s1
s2 = xxxxxxxxxxx
s1 = xxxx
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1
        
        if count_s1 == count_s2:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            count_s2[ord(s2[right]) - ord('a')] += 1
            count_s2[ord(s2[left]) - ord('a')] -= 1
            if count_s1 == count_s2:
                return True
            left += 1
        return False