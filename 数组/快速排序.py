def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float))else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
print(quickSort([47,29,71,99,78,19,24,47]))


def quick_sort(arr, start, end):  
    # 递归条件出口  
    if start >= end:  
        return   
    pivot = arr[start]  
    # 定义前后指针  
    low = start  
    high = end  
    # 如果前后2个指针不重合  
    while low < high:  
        # 从后向前走，直到遇到比自己还小的  
        while low < high and arr[high] >= pivot:  
            high -= 1  
        arr[low] = arr[high] # 这时候以high为index的位置是空着的  
         # 从前向后走，直到遇到比自己还小的  
        while low < high and arr[low] < pivot:  
            low += 1  
        arr[high] = arr[low] # 这时候high的位置被填充，但low为index位置为空  

        # 2边这时候都已经无法继续向下走  
        # 我们把中间这个数值和目前已经为空的以low为index的数值进行交换  
        arr[low] = pivot  
    # 这时候继续从左边进行递归，每次都缩小1个index的范围  
    quick_sort(arr,start,low - 1)  
    # 这时候继续从右边边进行递归，每次都增加1个index的范围  
    quick_sort(arr,high + 1, end)  


arr = [54,26,93,17,77,31,44,55,20]  
# end的代指最后一个数值的index，也就是长度-1  
quick_sort(arr,0,len(arr)-1)  
print(arr)  