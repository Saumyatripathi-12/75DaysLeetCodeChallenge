from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        # Find next greater for nums2
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            
            stack.append(num)
        
        # Remaining elements have no next greater
        while stack:
            next_greater[stack.pop()] = -1
        
        # Build answer for nums1
        return [next_greater[num] for num in nums1]
        