# 코드참고
# https://ratsgo.github.io/data%20structure&algorithm/2017/10/03/mergesort/

def counting_sort(A, k):
    B = [-1] * len(A)
    C = [0] * (k + 1)

    for a in A:
        C[a] += 1
    
    for i in range(k):
        C[i+1] += C[i]
    
    for j in reversed(range(len(A))):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1
    
    return B