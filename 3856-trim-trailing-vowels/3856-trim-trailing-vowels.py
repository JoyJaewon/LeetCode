'''
- return all the trailing vowels from the string

test cases
 case -> cas
 i -> ''
 test -> test

- make the string into the array
- make the vowel set
- while the last element in the array is vowel,
    -  pop
- if not return ''.join(array)

TC: O(N), SC: O(N)

'''
class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        s_arr = list(s)

        while s_arr and s_arr[-1] in vowel_set:
            s_arr.pop()
        
        return ''.join(s_arr)