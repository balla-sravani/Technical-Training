def check(arr, t, n):
    if t == 0:
        return True
    if n == 0:
        return False
        
    if arr[n-1] > t:
        return check(arr, t, n-1)
        
    return check(arr, t-arr[n-1], n-1) or check(arr, t, n-1)


arr = l=[2,3,5,6]
t = 12
ans = check(arr, t, len(arr))
if ans == True:
    print("yes")
else:
    print("no")
 

