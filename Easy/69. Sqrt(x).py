# 67.57% Runtime
# 87.34% Memory

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0:
            return 0
        if x < 4:
            return 1
        
        def Binary_Search(target: int, low: int, high: int) -> int:
            if low > high:
                return -1
            mid = (low + high) // 2
            
            if mid ** 2 == target or (mid ** 2 < target and (mid + 1) ** 2 > target):
                return mid
            if mid ** 2 < target:
                return Binary_Search(target, mid + 1, high)
            if mid ** 2 > target:
                return Binary_Search(target, low, mid - 1)
            return -1
        
        return Binary_Search(x, 1, x // 2)