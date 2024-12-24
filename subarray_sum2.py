def solve(ind,ds):
    ans.append(list(ds))
    for i in range(ind,len(arr)):
        if i!=ind and arr[i] == arr[i-1]:
            continue
        ds.append(arr[i])
        solve(i+1,ds)
        ds.pop(-1)


arr = [1,2,2]
ans = []
solve(0,[])
print(ans)