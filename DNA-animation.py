import time
rows = [
        "  o~~~~~~~0  ",
        "   o~~~~~0   ",
        "    o~~~0    ",
        "     o~0     ",
        "      @      ",
        "     0~o     ",
        "    0~~~o    ",
        "   0~~~~~o   ",
        "  0~~~~~~~o  "
        ]

iteration = 0

while True:
    time.sleep(.1)
    print(rows[iteration])
    iteration += 1
    if iteration > 8:
        iteration = 0
