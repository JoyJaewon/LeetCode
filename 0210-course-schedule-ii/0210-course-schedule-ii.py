class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = []
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for a, b in prerequisites: # b -> a
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque()

        for v in range(numCourses):
            if indegree[v] == 0:
                queue.append(v)
        
        while queue:
            curr_v = queue.popleft()
            visited.append(curr_v)
            for next_v in graph[curr_v]:
                indegree[next_v] -= 1
                if indegree[next_v] == 0:
                    queue.append(next_v)
        
        if len(visited) != numCourses:
            return []
        
        return visited
        