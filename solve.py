# New scramble R2 U D2 R' D2 U2 L R D2 F2 R F2 L' D2 B' F2 U F' R' U
edge = [22, 23, 17, 16, 21, 20, 19, 18, 4, 5, 12, 13, 9, 8, 14, 15, 1, 0, 11, 10, 6, 7, 3, 2]

cor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
#edge = [23, 22, 17, 16, 20, 21, 1, 0, 12, 13, 6, 7, 5, 4, 2, 3, 9, 8, 19, 18, 14, 15, 11, 10]
corner = [20, 19, 18, 17, 16, 15, 14, 13, 12, ]

def printMoves(argument):
    switcher = {
        1: "U, L U L F' L' F U' L' R' U' R' F R F' U R U'",  # Orange Yellow (1, 0)
        2: "Switch",                                    # Yellow Red (2, 3)
        3: "L, U', F, U, Switch, U', F', U, L'",        # Red Yellow (3, 2)
        4: "R2, U', R2, Switch, R2, U, R2",             # Yellow Blue (4, 5)
        5: "R', B, L, R, Switch, R', L', B', R",        # Blue Yellow (5, 4)
        6: "R2, R, R2, Switch, R2, R' R2",              # Yellow Green (6, 7)
        7: "U', F', U, L', Switch, L, U', F, U",        # Green Yellow (7, 6)
        8: "U2, R', U2, Switch, U2, R U2",              # Blue Orange (8, 9)
        9: "U, B, U', Switch, U, B', U'",               # Orange Blue (9, 8)
        10: "U', F' U, Switch, U', F, U",               # Orange Green (10, 11)
        11: "U2,  R, U2, Switch, U2, R', U2",           # Green Orange (11, 10)
        12: "L', Switch, L",                            # Green Red (12, 13)
        13: "U', F', U, Switch, U' F",                  # Red Green (13, 12)
        14: "U, B' U', Switch, U, B, U'",               # Red Blue (14, 15)
        15: "L, Switch, L'",                            # Blue Red (15, 14)
        16: "D2, L2, Switch, L2, D2",                   # White Orange (16, 17)
        17: "D', U', F, U, L', Switch, L, U', F', U, D",  # Orange White (17, 16)
        18: "L2, Switch, L2",                           # White Red (18, 19)
        19: "L', U', F, U, Switch, U', F', U, L",       # Red White (19, 18)
        20: "D, L2, Switch, L2, D'",                    # White Blue (20, 21)
        21: "U, B' U', L, Switch, L', U, B, U'",        # Blue White (21, 20)
        22: "D', L2, Switch, L2, D",                    # White Green (22, 23)
        23: "U', F, U, L', Switch, L, U', F', U"        # Green White (23, 22)
    }
    print(switcher.get(argument))

# Solving Edges
solvedEdge = 0

while solvedEdge == 0:
    if edge[0] == 0: # if buffer == 0
       for x in range(24):
           if cor[x] != edge[x]:
               printMoves(x)
               tmp1 = edge[0]
               tmp2 = edge[1]
               edge[0] = edge[x]
               edge[1] = edge[x + 1]
               edge[x] = tmp1
               edge[x + 1] = tmp2
               break
    elif edge[0] == 1:
       for x in range(1, 23):
           if cor[x] != edge[x] and edge[x] % 2 != 0:
               printMoves(x)
               tmp1 = edge[0]
               tmp2 = edge[1]
               edge[0] = edge[x]
               edge[1] = edge[x + 1]
               edge[x] = tmp1
               edge[x + 1] = tmp2
               break



    switchPos = 0
    found = 0

    while found == 0: # Look for position to be switched with
        if edge[0] == cor[switchPos]:
            found = 1
        else:
            switchPos += 1

    # Switch
    printMoves(switchPos)
    if switchPos % 2 == 0:
        tmp1 = edge[0]
        tmp2 = edge[1]
        edge[0] = edge[switchPos]
        edge[1] = edge[switchPos + 1]
        edge[switchPos] = tmp1
        edge[switchPos + 1] = tmp2
    else:
        tmp1 = edge[0]
        tmp2 = edge[1]
        edge[0] = edge[switchPos]
        edge[1] = edge[switchPos - 1]
        edge[switchPos] = tmp1
        edge[switchPos - 1] = tmp2

    # Check if solvedEdge
    solvedtmp = 1
    for x in range(24):
        if cor[x] != edge[x]:
            solvedtmp = 0

    if solvedtmp == 1:
        solvedEdge = 1

# Solving Corners


