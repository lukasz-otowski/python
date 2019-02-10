inp = str(input("Input a numbers divided by space: "))

# change all element in list into integers
inp = list(map(int, inp.split()))

iteration = 0
curr = 0

while iteration < len(inp):
    if curr < inp[iteration]:
        curr = inp[iteration]

    if iteration == len(inp):
        break
    else:
        iteration += 1

print('\n', "The highest number is: ", curr)
