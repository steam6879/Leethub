class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Build graph and indegree
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        # Add all 0 indegree courses to queue
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        completed = 0
        
        # Process courses level by level
        while queue:
            curr = queue.popleft()
            completed += 1
            
            # Reduce indegree for all dependent courses
            for next_course in graph[curr]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
                    
        return completed == numCourses
    