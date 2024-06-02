class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 10:
            square_sum = 0
            for num in str(n):
                square_sum += int(num) ** 2
            n = square_sum
        if n != 1 and n != 7 and n != 10:
            return False
        return True
    
print(Solution().isHappy(19))