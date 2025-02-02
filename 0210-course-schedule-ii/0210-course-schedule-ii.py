from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        que = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)

        ans = []
        while que:
            curr = que.popleft()
            ans.append(curr)

            for next_course in graph[curr]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    que.append(next_course)

        if len(ans) != numCourses:
            return []
        
        return ans
