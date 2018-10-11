import time
rows = [
		"  o~~~~~~~O  ",
		"   o~~~~~O   ",
		"    o~~~O    ",
		"     o~O     ",
		"      @      ",
		"     O~o     ",
		"    O~~~o    ",
		"   O~~~~~o   ",
		"  O~~~~~~~o  "
		]

iter = 0

while True:
	time.sleep(.1)
	print(rows[iter])
	iter +=1
	if iter > 8:
		iter = 0