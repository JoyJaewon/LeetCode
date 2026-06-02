'''
[1,2,3,1,4]
1: on -> off
2: on
3: on
4: on
-> [2,3,4] (sort)

- iterate through the array
    - initialize the set
    - if the current element is in the set, remove it
    - if not, add to the set
- return sort(set)

O(n) / O(n)
'''

class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        num_set = set()
        for bulb in bulbs:  #[1,2,3,1,4]
            if bulb in num_set:
                num_set.remove(bulb)
            else:
                num_set.add(bulb) #[2,3,4]
        return sorted(num_set)