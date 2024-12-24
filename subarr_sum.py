def solve(ind,sum):
    if ind >= len(arr):
        ans.append(sum)
        return
    solve(ind+1,sum+arr[ind])
    solve(ind+1,sum)

    

ans = []
arr = [2,4,1]
solve(0,0)
print(ans)