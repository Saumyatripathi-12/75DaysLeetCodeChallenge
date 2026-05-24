import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Convert list into max heap using negative values
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        # Remove largest element k-1 times
        for _ in range(k - 1):
            heapq.heappop(max_heap)

        # kth largest element
        return -heapq.heappop(max_heap)