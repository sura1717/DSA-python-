def solve(ind,rem,temparr):
    if rem ==0:
        ans.append(list(temparr))
        return
    if rem < 0:
        return

    for i in range(ind,len(arr)):
        if i>ind and arr[i] == arr[i-1]:
            continue
        if arr[i] > rem:
            return
        temparr.append(arr[i])
        solve(i+1,rem-arr[i],temparr)
        temparr.pop()




arr = [2,5,2,1,2]
arr.sort()
target = 5
ans = []

solve(0,target,[])
print(arr)
print(ans)
