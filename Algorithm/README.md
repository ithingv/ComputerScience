
<div align='center'>
  <h1>Sorting</h1>
</div>


## Table of Contents
**Sort Algorithm**
- [Table of Contents](#table-of-contents)
  - [#1](#1)
- [Quicksort](#quicksort)
  - [#2](#2)
- [Merge Sort](#merge-sort)
  - [#3](#3)
- [Heap Sort](#heap-sort)
  - [#4](#4)
- [Counting Sort](#counting-sort)
  - [#6](#6)
    - [References](#references)



---
### #1
## Quicksort
- [파이썬구현](./sorting/quick_sort.py)
- **퀵 정렬**(Quick sort)은 다른 원소와의 비교를 통해 데이터를 정렬하는 **비교 알고리즘**으로 **피벗**을 가지는 것이 특징이며 n개의 데이터를 정렬할 때, 어떤 피벗을 선택하는지에 따라 최악의 경우에는 O(n2)번의 비교를 수행하고, 평균적으로 O(n log n)번의 비교를 수행한다. 
- **퀵정렬라고 불리는 이유는 무엇일까?**
  - 퀵 정렬의 내부 루프는 대부분의 컴퓨터 아키텍처에서 효율적으로 작동하도록 설계되어 있고(메모리 참조가 지역화되어 있기 때문에 CPU 캐시의 히트율이 높아지기 때문이다.), 대부분의 실질적인 데이터를 정렬할 때 제곱 시간이 걸릴 확률이 거의 없도록 알고리즘을 설계하는 것이 가능하다. 또한 매 단계에서 적어도 1개의 원소가 자기 자리를 찾게 되므로 이후 정렬할 개수가 줄어든다. 때문에 일반적인 경우 퀵 정렬은 다른 O(n log n) 알고리즘에 비해 훨씬 빠르게 동작한다.
  - 원소들 중에 같은 값이 있는 경우 같은 값들의 정렬 이후 순서가 초기 순서와 달라질 수 있어 **불안정 정렬**에 속한다.
- **알고리즘**
    ```
    퀵 정렬은 분할 정복(divide and conquer) 방법을 통해 리스트를 정렬한다.
    1. 리스트 가운데서 하나의 원소를 고른다. 이렇게 고른 원소를 피벗이라고 한다.
    2. 피벗 앞에는 피벗보다 값이 작은 모든 원소들이 오고, 피벗 뒤에는 피벗보다 값이 큰 모든 원소들이 오도록 피벗을 기준으로 리스트를 둘로 나눈다. 이렇게 리스트를 둘로 나누는 것을 분할이라고 한다. 
    3. 분할을 마친 뒤에 피벗은 더 이상 움직이지 않는다.
    4. 분할된 두 개의 작은 리스트에 대해 재귀(Recursion)적으로 이 과정을 반복한다. 재귀는 리스트의 크기가 0이나 1이 될 때까지 반복된다.
    5. 재귀 호출이 한번 진행될 때마다 최소한 하나의 원소는 최종적으로 위치가 정해지므로, 이 알고리즘은 반드시 끝난다는 것을 보장할 수 있다.
    ```
- **복잡도**
    ```
    최악 시간복잡도: O(n2)
    최선 시간복잡도: O(n log n)
    평균 시간복잡도: O(n log n)
    ```
- **시각화**
<img src='/Algorithm/sorting/images/quick-sort.gif'>
<div align='center'>
    <img src='/Algorithm/sorting/images/quick_1.jpg'>
    <img src='/Algorithm/sorting/images/quick_2.jpg'>
    <img src='/Algorithm/sorting/images/quick_3.jpg'>
</div>
<br>

### #2 
## Merge Sort
- [파이썬구현](./sorting/merge_sort.py)
- **합병 정렬**(merge sort)은 **O(n log n)** 비교 기반 정렬 알고리즘이다. 일반적인 방법으로 구현했을 때 이 정렬은 **안정 정렬**에 속하며, 분할 정복 알고리즘의 하나이다.
- **알고리즘**
    ```markdown
    하향식 2-way 합병 정렬 동작 과정
    
    리스트의 길이가 1 이하이면 이미 정렬된 것으로 본다. 그렇지 않은 경우에는
    분할(divide) : 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
    정복(conquer) : 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
    결합(combine) : 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다. 이때 정렬 결과가 임시배열에 저장된다.
    복사(copy) : 임시 배열에 저장된 결과를 원래 배열에 복사한다.
    ```
- **복잡도**
   ```
   - 최악 시간복잡도: O(n log n)
   - 최선 시간복잡도: O(n log n)
   - 평균 시간복잡도: 일반적으로 O(n log n)
   - 공간복잡도: О(n)
   ```
- **시각화** 
<br>
<img src='/Algorithm/sorting/images/merge-sort.gif'>
<div align='center'>
    <img src='/Algorithm/sorting/images/merge_1.jpg'>
    <img src='/Algorithm/sorting/images/merge_2.jpg'>
    <img src='/Algorithm/sorting/images/merge_3.jpg'>
    <img src='/Algorithm/sorting/images/merge_4.jpg'>
    <img src='/Algorithm/sorting/images/merge_5.jpg'>
    <img src='/Algorithm/sorting/images/merge_6.jpg'>
</div>
<br>

---
### #3
## Heap Sort

---
### #4
## Counting Sort
- [파이썬구현](./sorting/counting_sort.py)
- **카운팅정렬**(counting sort)은 작은 양의 정수 key에 따라 원소를 정렬하는 알고리즘이다. 즉 **integer sotring** 알고리즘이다. 알고리즘은 고유한 key값을 가지는 객체의 수를 카운팅하고 출력 시퀀스에서 각 key값의 위치를 결정하기 위해 해당 카운트에 접두사(prefix)의 합을 적용하며 동작한다. 실행시간은 원소 수와 최소 key 값과 최대 key 값의 차이가 **선형적**이기 때문에 이 차이가 원소의 수보다 크게 크지 않은 경우에 사용하기 적합하다. 이 알고리즘은 더 큰 key를 효율적으로 다룰 수 있는 또 다른 정렬 알고리즘인 **기수정렬**(radix)에서 서브루틴으로 사용된다.
- **카운팅정렬**은 **비교정렬**이 아니며 key 값을 배열의 인덱스로 사용하고 **비교정렬**에 대한 하한 Ω(n log n)이 적용되지 않는다.
- **카운팅정렬** 대신 **버킷정렬**을 사용할 수 있으며 두 알고리즘은 유사한 성능을 가진다. 그러나 카운팅정렬과 비교해서 버킷정렬은 연결된 원소, 동적 배열 또는 각 버킷 내의 원소 집합을 저장하기 위해 미리 할당된 많은 메모리가 필요한 반면, 카운팅 정렬은 하나의 숫자(원소 수)를 저장한다.
- **알고리즘**
    ```
    A: Input array, b: output array, c: count array
    1. A로 부터 배열 내의 원소 값들의 갯수를 저장하는 count 배열(c)을 만든다.
    2. count array의 요소들에 대해 직전 요소들의 값을 더해준다.
    3. A와 동일한 크기의 출력을 담을 b를 만들고 입력 배열의 역순으로 출력 배열에 요소들을 채워넣는다.   
    ```
- **복잡도**
    ```
       최악의 시간복잡도: O(n+k), k는 양의 정수
       최악의 공간복잡도: O(n+k)
    ```
  - 시간복잡도 
    - count 배열의 초기화, count 배열에서 접두사(prefix)의 수를 세는 루프의 반복은 최대 k + 1회이고 따라서 O(k)이다. 그리고 출력 배열의 초기화는 O(n) 시간이 걸리므로 전체 알고리즘의 시간은 O(n + k)이다.
  
  - 공간복잡도
    - 길이 n, k+1의 배열을 사용하므로 사용하는 총 공간은 O(n + k)이다. 원소의 수보다 최대 key값이 훨씬 작은 경우, input과 output array외에 사용하는 저장 공간은 O(k)를 사용하는 Count 배열이기 때문에 이때 계수 정렬은 상당히 공간 효율적(high space efficient)이다.
    
- **시각화**

  ![](https://c.tenor.com/zswbYsLbYqEAAAAd/counting-sort.gif)
  
---
<div align='center'>
    <img src='/Algorithm/sorting/images/counting_1.jpg'>
    <img src='/Algorithm/sorting/images/counting_2.jpg'>
</div>

---
### #6
#### References
- [wikipedia](https://ko.wikipedia.org/)
- [ratsgo blog](https://ratsgo.github.io/)