'''
input: array of strings, string
output: integer - number of strings in the array that exist as a substring



- iterate through the array
    - check if the current element is in 'word'
    - if it is, +=1

- return count

TC: O(m*n), m = lenth of patterns, n = length of the word
SC: O(1)
'''
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0

        for pattern in patterns: 
            if pattern in word:
                count +=1
        
        return count
        