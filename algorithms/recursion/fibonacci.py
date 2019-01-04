def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibo(n-1) + fibo(n-2)

def fib(n, memo={}):
    if n == 0 or n == 1: return n

    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)

    return memo[n]
