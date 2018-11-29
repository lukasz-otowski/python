import random
#  template to copying
#  ,"                     "
#  ,"                     "
#  ,"                     "
#  ,"                     "
#  ,"                     "
#  ,"_____________________"
# please dont use word wrap to see all needed elements
elements = [
    ["  ###  ", "               ", "   ––#--  ", "              ", "   | [] [] [] [] |   ", "     ══════     ", "      ", "      <               ", "    ######/##     ", "               ", "                         "],
    [" ##### ", "               ", "    /|\   ", "              ", "   | [] [] [] [] |   ", "     ║ʳ  ʳ║     ", "      ", "     <        <       ", "     #\#####      ", "               ", "                         "],
    ["  ###  ", "               ", "          ", "      ____    ", "   | [] [] [] [] |   ", "     ║ʳ  ʳ║═══  ", "      ", "      <      <        ", "       ||/        ", "               ", "                         "],
    ["   | * ", "   _________   ", " #        ", "     /    \   ", "   | [] [] [] [] |   ", "  ═════  ʳ║ ʳ║  ", "   #  ", "               <      ", "    *--||         ", "               ", "        ____             "],
    ["   |/  ", "   |  _    |   ", " ##       ", "   _|   _  |  ", "   | []   _   [] |   ", "  ║ʳ ʳ║  ʳ║ ʳ║  ", "  #$  ", "                      ", "       ||-*       ", "     #     #   ", "   ___ / |-|  ___  ___   "],
    ["...|...", "_(_| | |   |_)_", "##########", "__/    { } |__", "___| []  | |  [] |___", "__║___║___║__║__", "_##$#_", "____##__%#__#....$##__", "....##.||...#.....", ".##.{#}..#{#}..", "__o--o_O---O__o--o_o--o__"]]

randEl = [random.randint(0, len(elements[0]) - 1),
          random.randint(0, len(elements[0]) - 1),
          random.randint(0, len(elements[0]) - 1),
          random.randint(0, len(elements[0]) - 1),
          random.randint(0, len(elements[0]) - 1),
          random.randint(0, len(elements[0]) - 1)]

for inner in range(6):
    print(elements[inner][randEl[0]],
          elements[inner][randEl[1]],
          elements[inner][randEl[2]],
          elements[inner][randEl[3]],
          elements[inner][randEl[4]],
          elements[inner][randEl[5]])
