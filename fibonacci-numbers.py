iterEnd = int(input("set number of iteration:"))

iter = 1
currFibNum = 1
fibList = []

while (iter < iterEnd):
    print(iter, currFibNum)
    fibList.append(currFibNum)
    iter += 1
    if iter > 2:
        currFibNum = 0
        currFibNum += fibList[-1] + fibList[-2]
    if iter == iterEnd:
        print("\nYour Fibonacci number is:")
        print(currFibNum)
