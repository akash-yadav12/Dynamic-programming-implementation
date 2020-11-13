#program to find the minimum difference of sum of a pair of subset eg: [1,3,4,5]--> s1= [1,5] s2 = [3,4] --> sum(s1) = 6 and sum(s2) = 7 ---> o/p 7-6 = 1
def subsetSum(ar,ra,n):
    for i in range(1,n+1):
        for j in range(1,ra+1):
            if ar[i-1] <= ra:
                dp[i][j] = dp[i-1][j-ar[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    

n = int(input('size of input'))
ar = list(map(int,input().split()))
ra = sum(ar)

dp = [[-1 for i in range(ra+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(ra+1):
        if i == 0:
            dp[i][j] = False
        if j == 0:
            dp[i][j] = True

subsetSum(ar,ra,n)
# print(dp)

el = []
for i in range((ra//2)+1):
    if dp[n][i]:
        el.append(i)
print(el)
mini = ra
for i in range(len(el)):
    mini = min(mini,(ra-(2*el[i])))
print(mini)