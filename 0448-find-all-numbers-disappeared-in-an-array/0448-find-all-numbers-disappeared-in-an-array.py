class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    
        n = len(nums)
        num_set = set(nums)
        result = []
        
        for i in range(1, n + 1):
            if i not in num_set:
                result.append(i)
        
        return result
