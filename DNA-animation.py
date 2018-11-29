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

iter = 0

while True:
    time.sleep(.1)
    print(rows[iter])
    iter += 1
    if iter > 8:
        iter = 0
