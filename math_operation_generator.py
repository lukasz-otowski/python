# WORKING DRAFT
# TO DO:
#   CODE DESCRIPTIONS
import random
import os


def do_operation(choice, integer_state, float_state):
    operation_element = [1, 2]
    # loop that make elements for equation
    for i in range(2):
        # when both type of equation elements is selected, first random type for each element
        # and then random value of element
        if integer_state == "✔" and float_state == "✔":
            element_type = random.choice(["integer", "float"])
            if element_type == "integer":
                operation_element[i] = random.randint(0, 100)
            elif element_type == "float":
                operation_element[i] = round(random.uniform(0, 100), 2)
        # random value for only integer type
        elif integer_state == "✔":
            operation_element[i] = random.randint(0, 100)
        # random value for only float type
        elif float_state == "✔":
            operation_element[i] = round(random.uniform(0, 100), 2)
        else:
            print("You chose: nothing :/")

    operation_result = None

    if choice == 1:
        operation_result = round(operation_element[0] + operation_element[1], 2)
        print(operation_element[0], " + ", operation_element[1])
    elif choice == 2:
        operation_result = round(operation_element[0] - operation_element[1], 2)
        print(operation_element[0], " - ", operation_element[1])
    elif choice == 3:
        operation_result = round(operation_element[0] * operation_element[1], 2)
        print(operation_element[0], " * ", operation_element[1])
    elif choice == 4:
        operation_result = round(operation_element[0] / operation_element[1], 2)
        print(operation_element[0], " / ", operation_element[1])
    else:
        print("That don't work...")

    required_type = type(operation_result)
    user_result = required_type(input())

    if user_result == operation_result:
        print("Dobrze!")
    elif user_result != operation_result:
        print("Źle!")


while True:
    # os.system('clear')
    current_loop_val = "?"
    changed_value = "?"
    global integer_status
    global float_status
    print("---M E N U---")
    print("Operation elements")
    try:
        integer_status and float_status
    except NameError:
        integer_status = "✔"
        float_status = "✔"
        print(integer_status, "Integer")
        print(float_status, "Float\n")
    else:
        print(integer_status, "Integer")
        print(float_status, "Float\n") 

    print("keyword           | input the keyword to execute the specific action")
    print("integer           | Change status of integer")
    print("float             | Change status of floating point number")
    print("operation         | Choice operation\n")
    menu_input = input()

    if menu_input == "keyword":
        print("INPUT THE KEYWORD TO EXECUTE THE SPECIFIC ACTION.")
    elif menu_input == ("float" or "integer"):
        if vars()[menu_input + "_status"] == "✔":
            vars()[menu_input + "_status"] = "✘"
        elif vars()[menu_input + "_status"] == "✘":
            vars()[menu_input + "_status"] = "✔"
    elif menu_input == "operation":
        # os.system('clear')
        print("---C H O I C E---")
        print("1 addition    3 multiplication")
        print("2 subtraction 4 dividing\n")
        print("Choice operation type")
        operation_type = input()
        do_operation(int(operation_type), integer_status, float_status)
