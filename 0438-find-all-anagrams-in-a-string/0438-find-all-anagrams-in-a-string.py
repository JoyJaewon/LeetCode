'''
input: s, p
output: list[int] - find the anagram of p in s and return the start inde
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        count_s = [0] * 26
        count_p = [0] * 26
        result = []

        for i in range(len(p)):
            count_p[ord(p[i]) - ord('a')] += 1
            count_s[ord(s[i]) - ord('a')] += 1
        
        if count_s == count_p:
            result.append(0)
        
        left = 0
        for right in range(len(p), len(s)):
            count_s[ord(s[right]) - ord('a')] += 1
            count_s[ord(s[left]) - ord('a')] -= 1
            left += 1
            if count_s == count_p:
                result.append(left)

        return result


        