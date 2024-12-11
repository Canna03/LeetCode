from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        even = (len(nums1) + len(nums2)) % 2 == 0
        median_position = (len(nums1) + len(nums2)) // 2
        
        prev = 0
        curr = 0
        
        while median_position > 0 and nums1 and nums2:
            prev = curr
            if nums1[0] < nums2[0]:
                curr = nums1.pop(0)
            else:
                curr = nums2.pop(0)
        
        if median_position > 0:
            if nums1:
                curr = nums1[median_position]
                if median_position > 1:
                    prev = nums1[median_position - 1]
            else:
                curr = nums2[median_position]
                if median_position > 1:
                    prev = nums2[median_position - 1]
            
        if even:
            return (prev + curr) / 2
        return curr
        
        
nums1 = [1,3]
nums2 = [2]

print(Solution().findMedianSortedArrays(nums1, nums2))