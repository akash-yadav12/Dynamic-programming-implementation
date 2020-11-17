def getMaxProf(wt,val,W,n):
    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]<= j:
                dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    return dp[n][W]


W = int(input('enter capacity of knapsack:'))
n = int(input('enter no of weight:'))
wt = list(map(int,input('enter weights:').split()))
val = list(map(int,input('enter vallues:').split()))

dp = [[-1 for i in range(W+1)] for j in range(n+1)]
for i in range(n+1):
    dp[i][0] = 0
for j in range(W+1):
    dp[0][j] = 0

res = getMaxProf(wt,val,W,n)
print(res)