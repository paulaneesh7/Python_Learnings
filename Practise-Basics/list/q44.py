# Generate Prime Numbers using List Comprehension

# for x in range(2, 20):
#     for num in range(2, x):
#         if x % num == 0:
#             break

def generate_primes(n):
    
    ans = [x for x in range(2, n) if all(x % num != 0 for num in range(2, int(x**0.5) + 1))]
    
    return ans



print(generate_primes(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]