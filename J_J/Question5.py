

def generate_odd_numbers(n):
    lst = []

    for i in range(1, n+1):
        if i % 2 != 0:
            lst.append(i)
    
    return lst

def generate_odd_numbers2(n):
    return [i for i in range(1, n+1) if i % 2 != 0]


n = 10
result = generate_odd_numbers(n)
print(result)