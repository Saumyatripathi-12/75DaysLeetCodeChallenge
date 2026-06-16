class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # Sum without carry
            temp = (a ^ b) & MASK

            # Carry
            b = ((a & b) << 1) & MASK

            a = temp

        # Handle negative numbers
        return a if a <= MAX_INT else ~(a ^ MASK)