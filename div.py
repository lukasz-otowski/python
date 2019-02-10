import random

divider = random.randrange(1, 11)
dividendBasis = random.randrange(1, 101)
dividend = dividendBasis * divider
divResult = int(dividend / divider)

print("\n", dividend, " / ", divider, " = ? ")
inp = int(input("what's the score: "))

if inp == divResult:
    print("\n", "Right!")
    print(dividend, " / ", divider, " = ", divResult)
elif inp != divResult:
    print("\n", "Bad!")
    print(dividend, " / ", divider, " = ", divResult)
