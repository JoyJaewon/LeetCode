class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            char_dict[s[right]] = char_dict.get(s[right], 0) + 1

            while (right - left + 1) - max(char_dict.values()) > k:
                char_dict[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        
        return longest