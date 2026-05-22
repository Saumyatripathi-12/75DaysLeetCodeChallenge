import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

        # Convert list into min heap
        heapq.heapify(self.heap)

        # Keep only k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        
        # If heap size is less than k
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)

        # If new value is larger than smallest
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        # Root of heap is kth largest
        return self.heap[0]

