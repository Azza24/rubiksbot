cor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
edge = [23, 22, 17, 16, 20, 21, 1, 0, 12, 13, 6, 7, 5, 4, 2, 3, 9, 8, 19, 18, 14, 15, 11, 10]

def printMoves(argument):
    switcher = {
        0: "Nothing?",                                  # Yellow Orange (0, 1) Solved
        1: "Flip buffer / don't know how yet lel",      # Orange Yellow (1, 0)
        2: "Switch",                                    # Yellow Red (2, 3)
        3: "L, U', F, U, Switch, U', F', U, L'",        # Red Yellow (3, 2)
        4: "R2, U', R2, Switch, R2, U, R2",             # Yellow Blue (4, 5)
        5: "R', B, L, R, Switch, R', L', B', R",        # Blue Yellow (5, 4)
        6: "R2, R, R2, Switch, R2, R' R2",              # Yellow Green (6, 7)
        7: "F' L', Switch, L, F",                       # Green Yellow (7, 6)
        8: "U2, R', U2, Switch, U2, R U2",              # Blue Orange (8, 9)
        9: "U, B, U', Switch, U, B', U'",               # Orange Blue (9, 8)
        10: "U', F' U, Switch, U', F, U",               # Orange Green (10, 11)
        11: "U2,  R, U2, Switch, U2, R', U2",           # Green Orange (11, 10)
        12: "L', Switch, L",                            # Green Red (12, 13)
        13: "U', F', U, Switch, U' F",                  # Red Green (13, 12)
        14: "U, B' U', Switch, U, B, U'",               # Red Blue (14, 15)
        15: "L, Switch, L'",                            # Blue Red (15, 14)
        16: "D2, L2, Switch, L2, D2",                   # White Orange (16, 17)
        17: "D, U', F, U, L', Switch, L, U', F', U, D'",  # Orange White (17, 16)
        18: "L2, Switch, L2",                           # White Red (18, 19)
        19: "L', U', F, U, Switch, U', F', U, L",       # Red White (19, 18)
        20: "D', L2, Switch, L2, D",                    # White Blue (20, 21)
        21: "U, B' U', L, Switch, L', U, B, U'",        # Blue White (21, 20)
        22: "D, L2, Switch, L2, D'",                    # White Green (22, 23)
        23: "U', F, U, L', Switch, L, U', F', U"        # Green White (23, 22)
    }
    print(switcher.get(argument))

solved = 0

while solved == 0:
    if edge[0] == 0: # if buffer == 0
       for x in range(24):
           if cor[x] != edge[x]:
               tmp = edge[x]
               edge[0] = edge[x]
               edge[x] = tmp


    switchPos = 0
    found = 0

    while found == 0: # Look for position to be switched with
        if edge[0] == cor[switchPos]:
            found = 1
        else:
            switchPos = switchPos + 2

    # Switch
    printMoves(switchPos)
    tmp = edge[0]
    edge[0] = edge[switchPos]
    edge[switchPos] = tmp

    # Check if solved
    solvedtmp = 1
    for x in range(24):
        if cor[x] != edge[x]:
            solvedtmp = 0

    if solvedtmp == 1:
        solved = 1



