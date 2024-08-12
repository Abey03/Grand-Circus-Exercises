# Users input
num = int(input("Please enter a number: "))
# Prints all number within a range from 1 to num(users input)
for x in range(1,num):
    print(f"{x} {x ** 2} {x ** 3}")

# Prints the users(input) integer
print(f"{num} {num ** 2} {num ** 3}")
# Asks the user if they want to continue
repeat = input("Continue? (y/n(takes you to multiplication))")

# While loop that activates as long as the user selects "y"
while repeat == "y":
    # Users input
    num = int(input("Please enter a number: "))
    # Prints all number within a range from 1 to num(users input)
    for x in range(1,num):
        print(f"{x} {x ** 2} {x ** 3}")

    # Prints the users(input) integer
    print(f"{num} {num ** 2} {num ** 3}")
    # Asks the user if they want to continue
    repeat = input("Continue? (y/n(takes you to multiplication))")

while repeat == "n":
    multiply = int(input("Enter a number to multiply: "))
    for y in range(1,multiply):
        print(f"{y} {y * 1} {y * 2} {y * 3} {y * 4}")

    print(f"{multiply} {multiply * 1} {multiply * 2} {multiply * 3} {multiply * 4}")
