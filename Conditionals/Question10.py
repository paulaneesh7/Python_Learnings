

pet = input("Enter the pet species: ")
pet_age = int(input("Enter the age of the pet: "))

if pet == "Dog":
    if pet_age <= 2:
        print("Puppy Food")
    elif pet_age <= 7:
        print("Adult Dog Food")
elif pet == "Cat":
    if pet_age <= 2:
        print("Kitten Food")
    elif pet_age <= 5:
        print("Adult Cat Food")