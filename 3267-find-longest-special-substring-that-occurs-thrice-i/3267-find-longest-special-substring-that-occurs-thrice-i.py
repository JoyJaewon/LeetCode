'''
input: string
output: integer - length of the longest special substring of s which occurs at least thrice

Clarifications
- do characters need to next to each other? no
- can it occur more than three times? yes

Test Cases
'aaaa' -> 'a' 4번 등장, 'aa' 3번 등장 'aaa' 2번 등장 (X) => return 2 ('aa')
'abcaba' -> 'a' 3번 등장 => return 1 ('a')
'abcdef' => return 0

Approach)

'''
class Solution:
    def maximumLength(self, s: str) -> int:
        def is_valid(length):
            """
            Check if there is a special substring of the given length
            that appears at least 3 times and is made of the same character.
            """
            freq = {}
            for i in range(len(s) - length + 1):
                sub = s[i:i + length]
                
                # Check if the substring is made up of the same character
                if len(set(sub)) > 1:
                    continue
                
                if sub in freq:
                    freq[sub] += 1
                else:
                    freq[sub] = 1
                
                if freq[sub] >= 3:
                    return True
            return False

        # Binary search on the length of the special substring
        left, right = 1, len(s)
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                result = mid  # If a valid special substring exists, update result
                left = mid + 1  # Try to find a longer special substring
            else:
                right = mid - 1  # Otherwise, try shorter substrings
        
        return result
