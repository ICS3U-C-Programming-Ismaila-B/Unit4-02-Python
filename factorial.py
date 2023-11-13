def calculate_factorial():
    while True:
        try:
            # Get a whole number from the user
            user_input = int(input("Enter a whole number: "))

            if user_input < 0:
                print("Please enter a non-negative whole number.")
                continue  # Restart the loop if a negative number is entered
            else:
                break  # Exit the loop if a valid whole number is provided
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Calculate the factorial using a do..while loop
    factorial_result = 1
    current_number = 1

    while current_number <= user_input:
        factorial_result *= current_number
        current_number += 1

    # Display the result
    print(f"The factorial of {user_input} is: {factorial_result}")


# Call the function to run the program
calculate_factorial()
