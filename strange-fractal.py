inpnum = int(input('write number from 0 to 10000000: '))
id = 0

if inpnum < 0 or inpnum > 10000000:
	print('try again')
else:
	while id < inpnum:
		if id < 10:
			print(id)
			id += 1
		elif id < 100:
			print(id, id - 10)
			id += 1
		elif id < 1000:
			print(id, id - 10, id - 100)
			id += 1
		elif id < 10000:
			print(id, id - 10, id - 100, id - 1000)
			id += 1
		elif id < 100000:
			print(id, id - 10, id - 100, id - 1000, id - 10000)
			id += 1
		elif id < 1000000:
			print(id, id - 10, id - 100, id - 1000, id - 10000, id - 100000)
			id += 1
		elif id < 10000000:
			print(id, id - 10, id - 100, id - 1000, id - 10000, id - 100000, id - 1000000)
			id += 1
		else:
			print('end')
			
