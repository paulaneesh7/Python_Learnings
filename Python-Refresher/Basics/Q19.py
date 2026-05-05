
def prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True




def prime_tillRange(limit):
    list = []
    for i in range(1, limit+1):
        if(prime(i)):
            list.append(i)
    return list


print(prime_tillRange(20))