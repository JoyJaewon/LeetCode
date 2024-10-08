'''
input: list[int]
output: integer - highest altitude of a point

Clarifications
- the first element always start with 0
- altitude can be negative

Test Cases
[-5,1,5,0,-7] -> [0,-5,-4,1,1,-6] => 1
[-1,-2,-3] -> [0,-1,-3,-4] => 0
[1,2,3] -> [0,1,3,4] => 4

Approach 1) 2-pass with space O(N) - create a new array with the altitude
            use max() to find the highest altitude TC: O(N)

Approach 2) 1-pass with space O(1) - iterate over the array once, track the max altitude

Plan
- define the function taking the list as a parameter
    - initialize highest to 0
    - initialize previous to 0
    - iterate over the list
        - previous += list[current]
        - update highest
    - return highest

TC: O(N), SC: O(1)
'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        previous = 0

        for i in range(len(gain)):
            previous += gain[i]
            highest = max(highest, previous)
            
        return highest
        