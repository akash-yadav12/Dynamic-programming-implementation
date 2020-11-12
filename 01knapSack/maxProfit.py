def getMaxProf(wt,val,w,n):
    if n == 0 or w == 0:
        return 0
    elif wt[n-1] <= w:
        return max(val[n-1] + getMaxProf(wt,val,w-wt[n-1],n-1) , getMaxProf(wt,val,w,n-1))
    else:
        return getMaxProf(wt,val,w,n-1)



W = int(input('enter capacity of knapsack:'))
n = int(input('enter no of weight:'))
wt = list(map(int,input('enter weights:').split()))
val = list(map(int,input('enter vallues:').split()))

res = getMaxProf(wt,val,W,n)
print(res)