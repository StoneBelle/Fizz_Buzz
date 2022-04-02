# Write your code below this row 👇

# Create the 1-100 range for my program
for number in range(1, 101):
    if (number % 3) == 0 and (number % 5) == 0:
        print("FizzBuzz")
    elif (number % 3) == 0:
        print("Fizz")
    elif (number % 5) == 0:
        print("Buzz")
    else:
        print(number)

# Depending on the number, print the follow words:
# Number/3 = Fizz, Number/5 = Buzz, Number/both = FizzBuzz