from collections import deque
import sys
 
def dfs(v1):
    visit[v1] = True
    print(v1, end = ' ')
    for v2 in edge[v1]:
        if visit[v2] == False:
            dfs(v2)
 
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

    dfs(start)
