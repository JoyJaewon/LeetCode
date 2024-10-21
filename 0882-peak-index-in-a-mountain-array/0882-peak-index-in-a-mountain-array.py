'''
input: list[int]
output: integer - index of the peak element

Clarifications
- minimum length of the array will be 3, which means there will be at least 1 peak array
- there will be 1 peak element
- it is guranteed to increase then decrease

Test Cases
[1,2,3,1] -> 2 (3 is the peak element)

Approach 1) Brute Force - iterate over the array to find the peak element. O(N)
Approach 2) Binary Search 

Plan
- define the function taking the list as a parameter
    - initialize the left and right pointers
    - while left < right
        - initialzie the mid pointer
        - if the mid element is greater than the left element
            - move left pointer to mid + 1
        - else:
            - move right pointer to mid - 1
    - return the left index

TC: O(logn), SC: O(1)
'''
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        return left
        