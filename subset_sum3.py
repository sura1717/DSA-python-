def solve(start,rem,ds):
    if rem == 0 and len(ds) == n:
        ans.append(list(ds))
        return
    if start > 9 or len(ds) >= n :
        return

    ds.append(start)
    solve(start+1,rem-start,ds)
    ds.pop()
    solve(start+1,rem,ds)



n = 4
k = 1
ans = []
solve(1,k,[])
print(ans)
