'''
input: array - nums, integer - k
output: integer - total number of subarrays whose sum equals to k

Clarification
- Can k be 0 or negative? Yes
- Can the input array be empty? No
- Can the input array has duplicate values? Yes
- Can the output subarray contain duplicate values? Yes
- Can the output subarray has 1 value which is equal to k? Yes
- Is given array sorted? No
- Can we use same number multiple times? No

Test Cases
[1,1,1], 2 => 2  [1,1]- first, second [1,1]-second, third
[1,2,3], 3 => 2  [1,2], [3]
[1], 1 => [1]
[-1, -2, -3], -3 => [-1,-2], [-3]

Approach
approach 1) three nested loops. check the sum of every possible subarray and 
            count how many of them are equal to k
approach 2) use hash map to store cumulative sum at each index

Plan
- initialize the hash map to store the cumulative sum up to each index and set the count of sum 0 to 1
- initialize variables prefix_sum to 0 and count to 0
- iterate through the array
    - update the prefix_sum by adding the current element
    - calculate target_sum as prefix_sum - k
    - if target_sum exists in prefix_sum_count, add its count to count
    - update the count of prefix_sum in prefix_sum_count
- return total count

=> TC: O(N), SC: O(N)
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        seen = {0:1}
        count = 0

        for num in nums:
            curr_sum += num
            if curr_sum - k in seen:
                count += seen[curr_sum - k]
            seen[curr_sum] = seen.get(curr_sum, 0) + 1
        
        return count