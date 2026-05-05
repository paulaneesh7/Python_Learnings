
# Pure and Impure functions
def pure_chai(cups):
    return cups*10



total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups*10
    return total_chai



print("#####################################################")

# Recursive function
def pour_chai(n):
    if n == 0:
        return "No chai to pour"
    return pure_chai(n-1)



print(pour_chai(5))



print("#####################################################")


# Lamda function

chai_types = ["Green Tea", "Black Tea", "Masala Chai", "Lemon Chai"]


# list(filter(lambda fnc_name: perform operation, iterable)) -> as we want to filter our so used filter
strong_chai = list(filter(lambda x: "Strong" in x, chai_types))

print(strong_chai)