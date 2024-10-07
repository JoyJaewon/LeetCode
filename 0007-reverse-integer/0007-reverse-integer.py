class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        LOWER = -(2**31) 
        UPPER = 2**31 - 1  

        result = 0  
        sign = 1 if x > 0 else -1  

        x = abs(x)  
        while x > 0:  
            result = result * 10 + x % 10  
            x //= 10  

        result *= sign  

        if result < LOWER or result > UPPER:
            return 0
        
        return result

            