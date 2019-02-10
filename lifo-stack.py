import os


class Stack:
    def __init__(self):
        self.val = 5
        self.cap = 8
        self.fill = 4
        self.empty = "[_]"
        self.full = "[█]"


Stack = Stack()


# function to show current state of stack
def show(empty_char, full_char, empty_value, fill_value):
    for it in range(Stack.cap, 0, -1):
        if it <= fill_value:
            print(full_char)
            it += 1
        elif it <= empty_value:
            print(empty_char)
            it += 1


# function to add possibility for user to control stack
def choice():
    fill_val = 1
    print("write: \n1 to add \n2 to remove")
    print("write: \n11 to increase capacity \n22 to decrease capacity")
    # print("")
    choice = int(input("Input: "))
    if choice == 1:
        Stack.fill += 1
    elif choice == 2:
        Stack.fill -= 1
    elif choice == 11:
        Stack.cap += 1
    elif choice == 22:
        Stack.cap -= 1


# show stack data
iteration = 1
while iteration <= 2:
    os.system('cls')
    if iteration == 1:
        show(Stack.empty, Stack.full, Stack.cap, Stack.fill)
        choice()
        iteration += 1
    elif iteration == 2:
        empty_val = 6
        show(Stack.empty, Stack.full, Stack.cap, Stack.fill)
        choice()
