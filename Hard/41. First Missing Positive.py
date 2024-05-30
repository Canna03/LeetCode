from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > len(nums):
                nums[i] = len(nums) + 1
        
        for i in range(len(nums)):
            num = abs(nums[i])
            if num > len(nums):
                continue
            num -= 1
            if nums[num] > 0:
                nums[num] = -1 * nums[num]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1

print(Solution().firstMissingPositive([1]))