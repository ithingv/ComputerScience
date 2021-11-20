class RadixSort:
    def __init__(self, num):
        self.num = num

    def radix_sort(self):
        # 최대 digit을 알아보기 위해 가장 큰 수를 찾는다
        max1 = max(self.num) 
    
        base = 1
        while max1/base > 0: 
            self.count_sort(self.num, base) 
            base *= 10


    def count_sort(self, A, k):
        B = [-1] * len(A)
        C = [0] * (10) # 1의 자리, 10의 자리수만 비교하기 때문에 범위는 0~9이다

        for i in range(len(A)): # 각 element가 몇개있는지 C에 저장한다
            idx = (A[i]//k) 
            C[idx % 10] += 1
        
        for i in range(1,10): # C의 요소값들을누적값으로 변경
            C[i] += C[i-1]

        i = len(A)-1
        while i>=0:  # C 를 indexing해서 정렬된 리스트를 찾는다
            idx = (A[i]//k) 
            B[C[idx % 10] - 1] = A[i] 
            C[idx % 10] -= 1
            i -= 1

        # 기존 리스트에 COPY
        for i in range(len(A)): 
            A[i] = B[i]
