def merge(arr,s,mid,e):
    left = arr[:mid]
    right = arr[mid:]

    i=j=k=0
    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1

    while i<len(left):
        arr[k] = left[i]
        i += 1
        k+=1

    while j<len(right):
        arr[k] = right[j]
        j += 1
        k+=1


def merge_sort(arr):
    def solve(s,e):
        if e-s == 1:
            return
        mid = (s + e) // 2
        solve(s,mid)
        solve(mid,e)
        merge(arr,s,mid,e)
    solve(0,len(arr)-1)

arr = [4,2,6,2,3,2,3,5,6,2]
merge_sort(arr)
print(arr)