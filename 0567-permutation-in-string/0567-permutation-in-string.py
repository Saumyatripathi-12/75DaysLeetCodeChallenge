from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_count = Counter()
        
        left = 0
        
        for right in range(len(s2)):
            window_count[s2[right]] += 1
            
            # Keep window size equal to len(s1)
            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1
                
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                
                left += 1
            
            # Compare frequency maps
            if window_count == s1_count:
                return True
        
        return False
        