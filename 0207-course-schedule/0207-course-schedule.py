class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 1. Initialize graph with dictionary
        graph = {i: [] for i in range(numCourses)}
        
        # 2. Build prerequisite relationships
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        # 3. Initialize tracking sets    
        seen = set()   # Tracks completed courses
        path = set()   # Tracks current DFS path
        
        def dfs(course):
            # Base case 1: Cycle detection
            if course in path:
                return False
                
            # Base case 2: Already verified course
            if course in seen:
                return True
            
            # Add course to current path    
            path.add(course)
            
            # Check all prerequisites
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            # Remove from path after processing
            path.remove(course)
            # Mark as completed
            seen.add(course)
            return True
            
        # 4. Verify each course
        return all(dfs(course) for course in range(numCourses))