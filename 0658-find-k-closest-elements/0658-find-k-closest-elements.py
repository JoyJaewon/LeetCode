'''
input: list - sorted, integer k, inter x
output: list - k closets integer to x

Clarifications
- can there be negative numbers? yes
- can there be duplciate numbers? yes
- if their absolute difference is same, choose smaller number

Test Cases
[1,2,3,4,5], k = 4, x = 3 -> [1,2,3,4]
[1,2,3,4,5], k = 3, x = 3 -> [2,3,4]
[1,2,3,4,5], k = 4, x = -1 -> [1,2,3,4]

Approach 1) use heap -> O(nlogn + klogk)
Approach 2) use binary search + sliding window


'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid 
        
        return arr[left:left + k]