num = int(input("Please enter a number: "))


if num % 2 != 0 and num < 60:
        print(num)
        print("Odd and less than 60")
elif num % 2 == 0 and num >= 2 and num <= 24:
        print(num)
        print("even and less than 25")
elif num % 2 == 0 and num >= 26 and num <= 60:
        print(num)
        print("Even and between 26 and 60 inclusive")
elif num % 2 == 0 and num > 60:
        print(num)
        print("Even and greater than 60")
elif num % 2 != 0 and num > 60:
        print(num)
        print("Odd and greater than 60")


