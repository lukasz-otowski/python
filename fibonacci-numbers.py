iterEnd = int(input("set number of iteration:"))

iteration = 1
currFibNum = 1
fibList = []

while iteration < iterEnd:
    print(iteration, currFibNum)
    fibList.append(currFibNum)
    iteration += 1
    if iteration > 2:
        currFibNum = 0
        currFibNum += fibList[-1] + fibList[-2]
    if iteration == iterEnd:
        print("\nYour Fibonacci number is:")
        print(currFibNum)
