from collections import deque

def bfs(start):

    queue = deque([start])
    visited[start] = True
    
    while queue:

        # 현재 정점
        curr_v = queue.popleft()
        print(f"{curr_v} ", end="")        
        for adj_v in edge_list[curr_v]:
    
            # 현재 정점과 인접한 노드 중 아직 방문하지 않은 노드라면 queue에 넣어준다.
            if not visited[adj_v]:
                queue.append(adj_v)
                visited[adj_v] = True # 방문 표시
        
if __name__ == "__main__":

    n = int(input())
    edge_list = [[] for _ in range(n + 1)]

    for i in range(n):
        e1, e2 = list(map(int, input().split()))
        edge_list[e1].append(e2)
        edge_list[e2].append(e1)

    visited = [False for _ in range(n + 1)]
    
    # 1번 정점부터 순회
    bfs(1)

    print(visited)
