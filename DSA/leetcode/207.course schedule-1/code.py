from collections import deque, defaultdict

def can_finish(numCourses, prerequisites):
    graph = defaultdict(list)
    
    indegree = [0] * numCourses
    
    for prerequisite in prerequisites:
        course, pre = prerequisite
        graph[pre].append(course)
        indegree[course] += 1
    
    queue = deque([c for c in range(numCourses) if indegree[c]==0])
    
    while queue:
        current = queue.popleft()
        
        for n in graph[current]:
            indegree[n] -= 1
            if indegree[n] == 0:
                queue.append(n)
    return sum(indegree) == 0


numCourses = 3
prerequisites = [[1,0], [0, 1], [1, 2]]
result = can_finish(numCourses, prerequisites)
print(result)