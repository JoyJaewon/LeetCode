'''
- output: index of the array (if multiple answer, return the smallest)
- "Minimum" capacity
- return -1 if no answer

- [1,5,3,7], 3
1 -> x, 5-> o, 3-> o, 7-> o
=> 5, 3, 7 are possible answers. since 3 is the smallest capacity, return 2(index)

- initialize val, index
- iterate through the array
    - if curr_val >= itemSize and curr_val < val, val = curr_val
    - index = curr_index
- if val = inf, return -1
- else return index

TC: O(N), SC: O(1)


'''
class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        val = float('inf')
        index = -1

        for i in range(len(capacity)):
            if capacity[i] >= itemSize and capacity[i] < val:
                val = capacity[i]
                index = i

        return index
        