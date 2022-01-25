from collections import deque

def dfs(v1):

    visited[v1] = True
    print(f"{v1} ", end="")

    for v2 in edge_list[v1]:
        if not visited[v2]:
            dfs(v2)


# def dfs(v1):
#     if visited[v1]:
#         return

#     visited[v1] = True
#     print(f"{v1} ", end="")
    
#     for v2 in edge_list[v1]:
#         dfs(v2)

if __name__ == "__main__":

    n = int(input())

    edge_list = [[] for _ in range(n + 1)]

    for i in range(n):
        e1, e2 = list(map(int, input().split()))
        edge_list[e1].append(e2)
        edge_list[e2].append(e1)

    visited = [False for _ in range(n + 1)]
    
    # 1번 정점부터 순회
    dfs(1)

    print(visited)
