# Print hello world
print('1. Print "hello world".')
print("hello world")


# Create a float variable
print('\n2. Create a float variable.')
my_float = 5.2
print(f"my_float = {my_float}")


# Create a string variable
print('\n3. Create a string variable.')
my_string = "My string variable"
print(f"my_string = {my_string}")


# Create a function that asks for your name and prints it with a sentence 'Hello my name is ???..!' to the console using f strings
print('\n4. Asking for the name and print greetings.')


def greet():
    name = input("What' your name? ")
    print(f"Hello my name is {name}!")


greet()


# Print the result for first 3 characters of the string on a new line
print('\n5. Print the result for first 3 characters of the string on a new line.\nInput string is "Python".')


def first_three_characters(str):
    return str[:3] if len(str) > 3 else str


print(first_three_characters('Python'))


# Print the result of the following math calc:
# 1+5 and then * (times) by 7 and then + 6
print('\n6. Print the result of the following math calc: ((1 + 5) * 7 + 6).')
print((1 + 5) * 7 + 6)


# Get the length of your variable string above and store it in a new variable
print('\n7. Get the length of your variable string above and store it in a new variable.')
string_length = len(my_string)
print(f"The length of \"{my_string}\" is {string_length}.")


# Create a Python list of numbers then sort it in reverse order, store the result in a new variable
print('\n8. Create a Python list of numbers then sort it in reverse order, store the result in a new variable.')
numbers = [3.5, 52, 54.99, 22, 543, 2.1]
new_numbers = sorted(numbers, reverse=True)
print(f"Original list of numbers: {numbers}")
print(f"New list of numbers: {new_numbers}")


# Use the same list of numbers and print out all the numbers that are less than a number entered via user input in the console
print('\n9. Print out all the numbers that are less than a number entered via user input in the console.')


def less_number():
    try:
        input_number = float(input("Pleas input a number: "))
    except ValueError:
        return("You didn't enter a valid number.\n")
    else:
        filtered = list(filter(lambda number: number < input_number, numbers))
        return(filtered)


print(less_number())
print()
