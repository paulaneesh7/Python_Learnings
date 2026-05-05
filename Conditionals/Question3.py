

grade = int(input("Enter your grade: "))

if grade >= 101:
    print("Invalid grade")
    exit()

if grade <= 100 and grade >= 90:
    print("A")
elif grade <= 89 and grade >= 80:
    print("B")
elif grade <= 79 and grade >= 70:
    print("C")
elif grade <= 69 and grade >= 60:
    print("D")
elif grade <= 59:
    print("F")