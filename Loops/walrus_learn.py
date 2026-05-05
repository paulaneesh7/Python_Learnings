value = 13

remainder = value % 3

if remainder:
    print(f"{value} is not divisible by 3, remainder is {remainder}")

if (remainder := value % 5):
    print(f"{value} is not divisible by 5, remainder is {remainder}")


available_sizes = ["S", "M", "L", "XL"]

if(requested_size := "M") in available_sizes:
    print(f"Size {requested_size} is available")