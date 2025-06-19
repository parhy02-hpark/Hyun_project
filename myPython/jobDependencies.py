'''
Write an algorithm that produces the order in which to run these jobs while respecting their dependencies.

Sample input/output: 

Jobs: [a, b]
Dependencies: [[b, a]]    
Output: b, a
'''

from collections import defaultdict, deque

def job_order(jobs, dependencies):
    # Step 1: Build graph and in-degree count
    graph = defaultdict(list)
    in_degree = {job: 0 for job in jobs}

    for prereq, job in dependencies:
        graph[prereq].append(job)
        in_degree[job] += 1

    # Step 2: Queue jobs with no dependencies (in-degree == 0)
    queue = deque([job for job in jobs if in_degree[job] == 0])
    result = []

    # Step 3: Process jobs in topological order
    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Detect cycle (if any jobs are left with non-zero in-degree)
    if len(result) != len(jobs):
        raise ValueError("Cycle detected in dependencies")

    return result


jobs = ['a', 'b']
dependencies = [['b', 'a']]
print(job_order(jobs, dependencies))

jobs2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
deps2 = [ ['a', 'b'], ['a', 'c'], ['b', 'd'], ['c', 'd'], ['e', 'f'], ['f', 'g'] ]
print(job_order(jobs2, deps2))
#exp2 = [a, e, b, f, c, d, g]
