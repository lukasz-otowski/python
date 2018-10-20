import os
import random
import time
#  template to copying
#  ,"                     "
#  ,"                     "
#  ,"                     "
#  ,"                     "
#  ,"                     "
#  ,"_____________________"
elements =[["[]","  ","  ","  ","  ","  ","  ","  ","  "],
           ["[]","[]","  ","  ","  ","  ","  ","  ","  "],
           ["[]","[]","[]","  ","  ","  ","  ","  ","  "],
           ["[]","[]","[]","[]","  ","  ","  ","  ","  "],
           ["[]","[]","[]","[]","[]","  ","  ","  ","  "],
           ["[]","[]","[]","[]","[]","[]","  ","  ","  "],
           ["[]","[]","[]","[]","[]","[]","[]","  ","  "],
           ["[]","[]","[]","[]","[]","[]","[]","[]","  "],
           ["[]","[]","[]","[]","[]","[]","[]","[]","[]"],]
indexV = [
            "9",
            "8",
            "7",
            "6",
            "5",
            "4",
            "3",
            "2",
            "1"
        ]
indexH = ["0","01","02","03","04","06","07","08","09"]

while True:
    os.system('cls')
    randEl = [random.randint(0,len(elements[0]) - 1),
              random.randint(0,len(elements[0]) - 1),
              random.randint(0,len(elements[0]) - 1),
              random.randint(0,len(elements[0]) - 1),
              random.randint(0,len(elements[0]) - 1),
              random.randint(0,len(elements[0]) - 1),
              random.randint(0,len(elements[0]) - 1),
              random.randint(0,len(elements[0]) - 1),]
    for inner in range(9):
        print(
                indexV[inner],
                elements[inner][randEl[0]],
                elements[inner][randEl[1]],
                elements[inner][randEl[2]],
                elements[inner][randEl[3]],
                elements[inner][randEl[4]],
                elements[inner][randEl[5]],
                elements[inner][randEl[6]],
                elements[inner][randEl[7]],
             )    
    print(indexH[0],indexH[1],indexH[2],indexH[3],indexH[4],indexH[5],indexH[6],indexH[7],indexH[8])
    time.sleep(.25)