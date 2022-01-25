def find_parent(parent, v1):
    if parent[v1] == v1: return v1
    return find_parent(parent, parent[v1])
    
    # 루트노드 서치 성능개선 
    # if parent[v1] != v1:
    #     return find_parent(parent, parent[v1])
    # return parent[v1]

def union_parent(parent, v1, v2):
    a = find_parent(parent, v1)
    b = find_parent(parent, v2)
    if a < b: parent[b] = a
    else: parent[a] = b 

if __name__ == "__main__":

    # 노드의 개수와 간선(Union 연산)의 개수 입력 받기
    v, e = map(int, input().split())
    parent = [0] * (v + 1) # 부모 테이블 초기화하기

    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i

    # Union 연산을 각각 수행
    for i in range(e):
        a, b = map(int, input().split())
        
        # 무방향 그래프 사이클 판별
        if find_parent(parent, a) == find_parent(parent, b):
            cycle = True
            print("cycle 발생")
            break
        else:
            union_parent(parent, a, b)

    # 각 원소가 속한 집합 출력하기
    print('각 원소가 속한 집합: ', end='')
    for i in range(1, v + 1):
        print(find_parent(parent, i), end=' ')

    print()

    # 부모 테이블 내용 출력하기
    print('부모 테이블: ', end='')
    for i in range(1, v + 1):
        print(parent[i], end=' ')


    # 사이클 판별
        # 유니온파인드 알고리즘을 이용해서 무방향 그래프 내에서 사이클을 판별할 수 있다.

        # 각 간선을 확인하면서 두 노드의 루트노드를 확인한다.
        # 1.1 루트 노드가 서로 다르면 -> union 연산 수행
        # 1.2 루트 노드가 서로 같으면 cycle 발생
        # 모든 간선에 대해 1 반복        