from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Build adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visiting = set()  # Current DFS path
        visited = set()   # Already processed

        def dfs(course):
            # Cycle detected
            if course in visiting:
                return False

            # Already checked
            if course in visited:
                return True

            visiting.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True