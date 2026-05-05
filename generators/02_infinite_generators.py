

def infinite_chai():
    count = 1
    while True:
        yield f"Refill {count}"
        count += 1


refill = infinite_chai()


n = int(input("How many refills do you want? "))

for _ in range(n):
    print(next(refill))


stall = infinite_chai()

st = int(input("How many refills do you want? "))


for _ in range(st):
    print(next(stall))