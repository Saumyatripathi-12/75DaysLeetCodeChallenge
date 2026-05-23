import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Python has min heap, so use negative values for max heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # Take two largest stones
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)

            # If stones are not equal
            if first != second:
                heapq.heappush(max_heap, -(first - second))

        # Return remaining stone or 0
        return -max_heap[0] if max_heap else 0