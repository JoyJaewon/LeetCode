'''
use dictionary to track the frequency in the window
aababba, 2
l
   r
{a:3, b:1} 
length - max(dict.values())
5 - 3 = 2
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        count = {}
        left = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)

        return longest

        