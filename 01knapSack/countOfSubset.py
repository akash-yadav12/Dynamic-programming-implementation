#program to get number of subset which can add up to give the given sum
def getCountSubset(ar,s,n):
    for i in range(1,n+1):
        for j in range(1,s+1):
            if ar[i-1]<=j:
                dp[i][j] = dp[i-1][j-ar[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)
    return dp[n][s]


n = int(input())
ar = list(map(int,input().split()))
s = int(input())

dp = [[-1 for i in range(s+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(s+1):
        if i == 0:
            dp[i][j] = 0
        if j == 0:
            dp[i][j] = 1
print(getCountSubset(ar,s,n))