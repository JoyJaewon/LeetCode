'''
input: list of weights and integer days
output: integer - least weight capacity of the ship that will be shipped within days

'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(mid):
            total_day = 1  
            curr = 0
            for weight in weights:
                if curr + weight <= mid:
                    curr += weight
                else:
                    total_day += 1
                    curr = weight

            return total_day <= days
        
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left  
