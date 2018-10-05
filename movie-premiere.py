import random
def movie_premiere():
	name = input('write your name: \n')
	###lists to storage movies titles
	movies_0 = [
		'Potter and the Chamber of Secrets',
		'Jones and the Kingdom of the Crystal Skull',
		'Gump',
		'on Fire'
		]
	movies_1 = [
		'The Lord of the Rings: The Return of the',
		'The Hobbit: The Desolation of',
		'Saving Private',
		'Dirty'
		]
	premiere_txt = 'Today we have premiere an awesome movie! \n'
	rand_list = random.randrange(0,3)
	
	###get a random movie title
	if rand_list == 0:
		rand_mov = random.randrange(0,len(movies_0))
		print(premiere_txt,'"',name,movies_0[rand_mov],'"')
	elif rand_list == 1:
		rand_mov = random.randrange(0,len(movies_1))
		print(premiere_txt,'"',movies_1[rand_mov],name,'"')
	else:
		print('Today we don\'t have anything movie premiere... \n Sorry', name, ':.(')

###call function
movie_premiere()