'''
input: array of integers
output: boolean. true if any element of the array has frequency of prime number

[1,1,2,3,4]
1:2, 2:1, 3:1, 4:1
=> true (1 has the frequency of 2 which is a prime number)

- iterate through the array and make dictionary o(n)
- iterate through the dictionary and check each value to determine if it's prime or not o(n)
    - if prime, return true => make helper function o(sqaure root of n)
- return false

TC: o(n * sqaure root of n), SC: O(n)

'''
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
        
        for count in num_dict.values():
            if self.isPrime(count):
                return True

        return False
    
    def isPrime(self, n: int):
        if n < 2:
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True
        