"""

Create a Python file named lab_10-1.py
*** You must write a comment for every chunk of code you write from now on along with your author tag***

Using a while loop, write a program that prompts the user to input a number.
If the user inputs a number, add that to the sum of the previous numbers entered.
If the user enters -1, the program should end and display the sum of all the numbers entered.
Be sure the program uses a break statement
"""
#author Jon Morris


# Initialize sum to 0
total_sum = 0

while True:
    try:
        # Prompt user for input
        user_input = float(input("Enter a number (or -1 to end): "))
        
        # Check if user entered -1
        if user_input == -1:
            break  # Exit the loop if -1 is entered
        
        # Add the input to the sum
        total_sum += user_input

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Display the sum of all numbers entered
print(f"Sum of all numbers entered: {total_sum}")

_____________________________________________________________________________________________________________
"""
Create a Python file named lab_10-2.py
Using the same approach as lab 1, write a program that prints all the numbers that are multiples of 3 in a list. Be sure your program uses a continue statement

"""
#Author Jon Morris

def print_multiples_of_three(numbers):
    """
    Prints all the numbers in the given list that are multiples of 3.
    """
    print("Numbers that are multiples of 3:")
    for num in numbers:
        # Check if the number is not a multiple of 3
        if num % 3 != 0:
            continue  # Skip to the next iteration if not a multiple of 3
        print(num)

# Test the function with a list of numbers
numbers_list = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27]
print_multiples_of_three(numbers_list)
