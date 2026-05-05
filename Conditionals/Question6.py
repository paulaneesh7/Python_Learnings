
distance = int(input("Enter Distance: "))

if distance < 3:
    print("Mode of Transportation: ", "Walking")
elif distance >= 3 and distance < 15:
    print("Mode of Transportation: ", "Bike")
elif distance >= 15:
    print("Mode of Transportation: ", "Car")