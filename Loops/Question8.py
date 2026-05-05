

# Prime Check

num = int(input("Enter a number: "))
check = True

for i in range(2, num):
    if num % i == 0:
        check = False
        break

if check:
    print("Prime")
else:
    print("Not Prime")