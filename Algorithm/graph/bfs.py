from collections import deque
import sys
 
def bfs():
    queue = deque([start])
    visit = [False for _ in range(n + 1)]
    visit[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in edge[v]:
            if not visit[i]:
                visit[i] = True
                queue.append(i)

if __name__ == "__main__":

    n, m, start = map(int, sys.stdin.readline().strip().split())
    
    edge = [[] for _ in range(n + 1)]
 
    for _ in range(m):
        v1, v2 = map(int, sys.stdin.readline().strip().split())
        edge[v1].append(v2)
        edge[v2].append(v1)
 
    for e in edge:
        e.sort()
 
    visit = [False for _ in range(n + 1)]

    bfs()
    print()