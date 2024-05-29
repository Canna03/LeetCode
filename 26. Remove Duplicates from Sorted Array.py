from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer_index = 0
        for index in range(1, len(nums)):
            if nums[index] < nums[pointer_index]:
                return pointer_index + 1
            if nums[index] > nums[pointer_index]:
                pointer_index += 1
                nums[index], nums[pointer_index] = nums[pointer_index], nums[index]
        return pointer_index + 1
