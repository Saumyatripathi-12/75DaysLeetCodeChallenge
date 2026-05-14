from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            # Calculate total hours needed at speed = mid
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid - 1) // mid   # ceil(pile/mid)

            # If Koko can finish within h hours
            if total_hours <= h:
                right = mid
            else:
                left = mid + 1

        return left