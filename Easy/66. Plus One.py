# 93.33% Runtime
# 83.09% Memory

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits == [9]*len(digits):
            return [1] + [0] * len(digits)
        
        index = len(digits) - 1
        digits[index] += 1
        while digits[index] == 10:
            digits[index] = 0
            index -= 1
            digits[index] += 1
        return digits