#program to check whether there is a pair of a subset which can sum up to give equal sum

def isSubset(arr,s1,n):
    for i in range(1,n+1):
        for j in range(1,s1+1):
            if arr[i-1] <= s1:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)
    return dp[n][s1]

n = int(input())
arr = list(map(int,input().split()))
s = sum(arr)
if s%2 == 0: 
    dp = [[-1 for i in range((s//2)+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range((s//2)+1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True
    # print(dp[0][0])
    print(isSubset(arr,s//2,n))
else:
    print(False)