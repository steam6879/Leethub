class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Build adjacency list using dictionary for faster lookups
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for course, prereq in prerequisites:
            graph[course].append(prereq)
            
        # Track visited and current path
        seen = set()
        path = set()
        
        def dfs(course):
            # Base cases for optimization
            if course in path:
                return False
            if course in seen:
                return True
                
            path.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
                    
            path.remove(course)
            seen.add(course)
            return True
            
        # Check each course
        for course in range(numCourses):
            if not dfs(course):
                return False
                
        return True