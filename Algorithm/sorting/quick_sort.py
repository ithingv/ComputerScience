# 코드참고
# https://ratsgo.github.io/data%20structure&algorithm/2017/09/28/quicksort/

# not inplace sort
def quick_sort_not_inplace(arr):
    if len(arr) <= 1:
        return arr 
    else:
        pivot_val = arr[0]
        leftArr = [elem for elem in arr[1:] if elem <= pivot_val]
        rightArr = [elem for elem in arr[1:] if elem > pivot_val]
        return quick_sort_not_inplace(leftArr) + [pivot_val] + quick_sort_not_inplace(rightArr)

# in place sort
def quick_sort_inplace(arr):
    quick_sort_helper(arr,0, len(arr)-1)

def quick_sort_helper(arr, start, end):
    if start < end:
        pivot_idx = partition(arr, start, end)

        quick_sort_helper(arr, start, pivot_idx - 1)
        quick_sort_helper(arr, pivot_idx + 1, end)
    
def partition(arr, start, end):
    pivot_value = arr[start]
    leftmark = start + 1
    rightmark = end
    done = False

    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivot_value:
            leftmark = leftmark + 1
        
        while arr[rightmark] >= pivot_value and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]

    arr[start], arr[rightmark] = arr[rightmark], arr[start]

    return rightmark 
