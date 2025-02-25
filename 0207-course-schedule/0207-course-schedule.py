from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        queue = deque()
        ans = []
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            curr_v = queue.popleft()
            ans.append(curr_v)
            for next_v in graph[curr_v]:
                indegree[next_v] -= 1
                if indegree[next_v] == 0:
                    queue.append(next_v)
        
        if len(ans) != numCourses:
            return False
        return True