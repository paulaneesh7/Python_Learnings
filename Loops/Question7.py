
# Validate Input

while True:
    try:
        input_str = input("Enter a string: ")
        
        if input_str >= 1 and input_str <= 100:
            print(f"Great! {input_str} is within the range.")
            break
        else:
            print(f"Sorry, {input_str} is not within the range. Please try again.")

    except ValueError:
        print(f"Sorry, {input_str} is not a valid input. Please try again.")


