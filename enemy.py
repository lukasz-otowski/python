import time
import random
import os


# class to create game players
class Player:
    def __init__(self, life, damage):
        self.life = life
        self.damage = damage


# create enemy and user players
enemy = Player(10, 3)
user = Player(10, 2)


# gameplay function
def gameplay():

    while enemy.life >= 1 and user.life >= 1:
        os.system('clear')
        print("Your life", user.life)
        print("Enemy life", enemy.life)
        time.sleep(.5)
        userMove = input("\n Your move: \n attack = a \n dodge = d \n")
        enemyMove = random.randint(0, 1)

        # user move
        if userMove == "d":
            # change enemy attack chance
            enemyMove = random.randint(0, 4)
        elif userMove == "a":
            # remove enemy life
            enemy.life -= 2

        # enemy move
        if enemyMove == 0:
            user.life -= enemy.damage

    # if enemy life is under 1 then user win
    if enemy.life < 1:
        print("\n YOU WIN !!!")
    # if user life is under 1 then enemy win
    elif user.life < 1:
        print("\n ENEMY WIN :(")


# turn on gameplay
gameplay()
