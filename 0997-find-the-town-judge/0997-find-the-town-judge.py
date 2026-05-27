from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # indegree[i] = how many people trust i
        # outdegree[i] = how many people i trusts
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1

        # Judge trusts nobody and trusted by everyone else
        for person in range(1, n + 1):
            if indegree[person] == n - 1 and outdegree[person] == 0:
                return person

        return -1