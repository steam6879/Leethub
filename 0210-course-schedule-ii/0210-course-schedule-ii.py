from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Initialize graph and in-degree counter
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build adjacency list and count prerequisites
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        # Find all courses with no prerequisites
        que = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)
        
        # Process courses in topological order
        ans = []
        while que:
            curr = que.popleft()
            ans.append(curr)

            # Reduce in-degree for all dependent courses
            for next_course in graph[curr]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    que.append(next_course)

        # Return result if all courses can be completed
        return ans if len(ans) == numCourses else []
