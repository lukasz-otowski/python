inp = str(input("Input a numbers divided by space: "))

#change all element in list into integers
inp = list(map(int, inp.split()))

iter = 0
curr = 0

while iter < len(inp):
	if curr < inp[iter]:
		curr = inp[iter]
	
	if iter == len(inp):
		break
	else:
		iter += 1
	
print('\n',"The highest number is: ", curr)