def fib_memo(n):
    if memo[n] != None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_memo(n-1) + fib_memo(n-2)
    memo[n] = result
    print(memo)
    return result

n = int(input())
memo = [None]*(n+1)
print(fib_memo(n))