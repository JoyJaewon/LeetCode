'''
- no valid pair / length of the array = 1 => return [-1, -1]
- smallest different frequenceis

Test cases
[1,2,2,2,3,4,5,5,6] => [1,5]
[1,1]=> [-1,-1]
[1] => [-1,-1]

Approach
- dictionary
- iterate through the array
    - make the dictionary
- sort the dictionary
- iterateve through the dictionary

TC: O(), SC: O(n)
'''
class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        if len(nums) < 2:
            return [-1, -1]
        num_dict = {}

        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
        
        sorted_keys = sorted(num_dict.keys())
        
        for i in range(len(sorted_keys)):   #o(n^2)
            for j in range(i + 1, len(sorted_keys)):
                x, y = sorted_keys[i], sorted_keys[j]
                if num_dict[x] != num_dict[y]:
                    return [x, y]
        
        return [-1, -1]

