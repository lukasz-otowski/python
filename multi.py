import random

# generate action numbers
first = random.randrange(1, 100)
second = random.randrange(1, 100)
result = first * second

# show a operation
print(first, " * ", second, " = ? ")
inpRes = int(input("Input result: "))

# check result
print("\n")
if inpRes == result:
    print("Good")
    print(first, " * ", second, " = ", result, "\n")
elif inpRes != result:
    print("Bad, right result is: ")
    print(first, " * ", second, " = ", result)
