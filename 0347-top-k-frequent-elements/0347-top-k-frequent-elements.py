from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        # Create buckets where index = frequency
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, c in count.items():
            freq[c].append(num)
        
        result = []
        # Traverse from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result