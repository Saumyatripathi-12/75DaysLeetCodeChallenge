from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # Count frequency of tasks
        count = Counter(tasks)

        # Max heap using negative frequencies
        max_heap = [-freq for freq in count.values()]
        heapq.heapify(max_heap)

        time = 0

        # Queue stores: [remaining_count, available_time]
        cooldown = deque()

        while max_heap or cooldown:
            time += 1

            # Execute most frequent task
            if max_heap:
                freq = 1 + heapq.heappop(max_heap)

                # If task still remains
                if freq != 0:
                    cooldown.append((freq, time + n))

            # Push task back after cooldown
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

        return time
        