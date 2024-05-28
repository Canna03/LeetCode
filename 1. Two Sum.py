from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in map:
                return [map[difference], i]
            map[nums[i]] = i
        return -1