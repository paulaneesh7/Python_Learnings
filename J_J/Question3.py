

def recusive_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recusive_fibo(n-1) + recusive_fibo(n-2)
    



print(recusive_fibo(10))