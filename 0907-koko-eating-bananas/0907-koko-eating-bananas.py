'''
[3,6,7,11], 8

1 + 11 // 2 = 6 한시간에 6개씩 먹을수 있는지 확인
1, 1, 2, 2 = 6 먹을수 있음. 그럼 조금더 천천히 먹어보자




'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def can_eat(k):
            time = 0
            for pile in piles:
                time += (pile + k - 1) // k
            
            return time <= h


        while left < right:
            mid = (left + right) // 2
            if can_eat(mid):
                right = mid
            
            else:
                left = mid + 1
        
        return right

        