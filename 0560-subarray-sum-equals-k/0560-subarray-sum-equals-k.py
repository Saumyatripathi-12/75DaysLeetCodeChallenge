from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        prefix_map = defaultdict(int)
        
        prefix_map[0] = 1  # base case
        
        for num in nums:
            prefix_sum += num
            
            if (prefix_sum - k) in prefix_map:
                count += prefix_map[prefix_sum - k]
            
            prefix_map[prefix_sum] += 1
        
        return count
        