'''
input: array
output: index of the target element (equal possibility)

Preprocess the array to store indices of each number, 
so the pick function can return a random index in O(1) time.
'''
class Solution:

    def __init__(self, nums: List[int]):
        self.dict = {}
        for i in range(len(nums)):
            if nums[i] not in self.dict:
                self.dict[nums[i]] = []
            self.dict[nums[i]].append(i)
 
        

    def pick(self, target: int) -> int:
        return random.choice(self.dict[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)