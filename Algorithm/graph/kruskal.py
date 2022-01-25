def kruskal(lst):
    min_val = 0
    while lst:

        # 간선이 모두 연결되었다면    
        if sum(parent) == v:
            break

        v1, v2, dist = lst.pop(0)
        # 사이클이 존재하는지 체크
        if find_parent(parent, v1) != find_parent(parent, v2):
            union_parent(parent, v1,v2)
            min_val += dist

    return min_val

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, v1, v2):
    a = find_parent(parent, v1)
    b = find_parent(parent, v2)
    if a < b: parent[b] = a
    else: parent[a] = b 


if __name__ == "__main__":

    # 정점의 개수, 간선
    v, e= map(int, input().split())

    parent = [0] * (v + 1)
    v_list = []

    parent = [ i for i in range(1, v + 1)]

    for i in range(e):
        v1, v2, dist = list(map(int, input().split()))
        v_list.append([v1, v2, dist])

    # 정렬
    v_list.sort(key=lambda x: (x[2], x[0], x[1]))
    print(kruskal(v_list))
