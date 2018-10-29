import time
import random
import os
inpName = str(input("Community name: "))
inpPers = int(input("Input a number of persons: "))
inpSkills = int(input("Input initial skills of your community: "))

class Community:
	def __init__(self, name, total, int_skl):
		self.name = name
		self.total_persons = total
		self.neutral_pers = total
		self.pleased_pers = 0
		self.bored_pers = 0
		self.initial_skills = int(total / 25) + 3
		self.current_skills = int(total / 25) + 3
		self.acquired_skills = 0
		self.new_employees = 0
	
	def print_status(self):
		print("Community: ", self.name)
		print("Total persons", self.total_persons)
		print("New employees", self.new_employees)
		print("Neutral persons", self.neutral_pers)
		print("Pleased persons", self.pleased_pers)
		print("Bored persons", self.bored_pers)
		print("Initial skills ", self.initial_skills)
		print("Current skills ", self.current_skills)
		print("Acquired skills ", self.acquired_skills)
	
	def inner_progress(self, current_day):
		if (self.neutral_pers - 4) > 0:
			bored = random.randint(0,1)
			pleased = random.randint(0,3)
			self.neutral_pers -= (pleased + bored)
			self.pleased_pers += pleased
			self.bored_pers += bored
		
		if self.neutral_pers < 10:
			rand_emp = random.randint(0,3)
			self.new_employees += rand_emp
			self.total_persons += rand_emp
			self.neutral_pers += rand_emp
		
		if self.new_employees > 0:
			self.acquired_skills += int((current_day / self.new_employees) / self.initial_skills)
			self.current_skills = self.initial_skills + self.acquired_skills

def communities_progress(pers1,pers2):
	comm_projects = int((pers1 + pers2) / 75)
	compl_train = int((pers1 + pers2) / 35)
	org_meets = int((pers1 + pers2) / 25)
	print("Common projects: ", comm_projects)
	print("Common training sessions: ", compl_train)
	print("Organized meetings: ", org_meets)
	comm_projects += 2
	compl_train += 4
	org_meets += 3
		
test = Community("Test group",231, 9)
new = Community(inpName,inpPers, inpSkills)

time.sleep(.5)
iter = 1
while True:
	os.system('cls')
	print("Day of communities contact: ", iter)
	print("\n")
	
	test.print_status()
	test.inner_progress(iter)
	
	print("\n")
	
	new.print_status()
	new.inner_progress(iter)
	
	print("\n")
	
	communities_progress(new.total_persons,test.total_persons)
	
	iter += 1
	time.sleep(.5)