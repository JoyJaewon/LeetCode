'''
input: 2 strings
output: 1 string - merged string

Clarifications
- the strings consist of lowercase only
- do we start with word1? yes
- can the characters be duplciated? yes

Test Cases
'abc', 'pqr' -> 'apbqcr'
'd', 'bbb' -> 'dbbb'
'aaa', 'b' -> 'abaa'
'a', 'b' -> 'ab'

Approach 
- convert the strings into lists and append the characters to the result list alternately

Plan
- define the function taking two strings as parameters
    - convert both strings into the lists
    - initialize n as the minimum length of word1 and word2
    - initialize an empty result list
    - iterate through the characters of both strings up to n
        - append the characters alternately to the result list
    - append the remaining characters
    - convert the list back to string and return

TC: O(N + M), SC: O(N)
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = max(len(word1), len(word2))
        result = []

        for i in range(n):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
                
        return ''.join(result)

        