# New scramble R2 U D2 R' D2 U2 L R D2 F2 R F2 L' D2 B' F2 U F' R' U
# edge = [22, 23, 17, 16, 21, 20, 19, 18, 5, 4, 12, 13, 9, 8, 14, 15, 1, 0, 11, 10, 6, 7, 3, 2]

cor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]


# corner = [20, 19, 18, 16, 15, 17, 14, 13, 12, 21, 23, 22, 5, 3, 4, 0, 1, 2, 10, 11, 8, 6, 0, 7]

def printMoves(argument):
    switcher = {
        1: "U, L U L F' L' F U' L' R' U' R' F R F' U R U'",  # Orange Yellow (1, 0)
        2: "Switch",  # Yellow Red (2, 3)
        3: "L, U', F, U, Switch, U', F', U, L'",  # Red Yellow (3, 2)
        4: "R2, U', R2, Switch, R2, U, R2",  # Yellow Blue (4, 5)
        5: "R', B, L, R, Switch, R', L', B', R",  # Blue Yellow (5, 4)
        6: "R2, R, R2, Switch, R2, R' R2",  # Yellow Green (6, 7)
        7: "U', F', U, L', Switch, L, U', F, U",  # Green Yellow (7, 6)
        8: "U2, R', U2, Switch, U2, R U2",  # Blue Orange (8, 9)
        9: "U, B, U', Switch, U, B', U'",  # Orange Blue (9, 8)
        10: "U', F' U, Switch, U', F, U",  # Orange Green (10, 11)
        11: "U2,  R, U2, Switch, U2, R', U2",  # Green Orange (11, 10)
        12: "L', Switch, L",  # Green Red (12, 13)
        13: "U', F', U, Switch, U' F",  # Red Green (13, 12)
        14: "U, B' U', Switch, U, B, U'",  # Red Blue (14, 15)
        15: "L, Switch, L'",  # Blue Red (15, 14)
        16: "D2, L2, Switch, L2, D2",  # White Orange (16, 17)
        17: "D', U', F, U, L', Switch, L, U', F', U, D",  # Orange White (17, 16)
        18: "L2, Switch, L2",  # White Red (18, 19)
        19: "L', U', F, U, Switch, U', F', U, L",  # Red White (19, 18)
        20: "D, L2, Switch, L2, D'",  # White Blue (20, 21)
        21: "U, B' U', L, Switch, L', U, B, U'",  # Blue White (21, 20)
        22: "D', L2, Switch, L2, D",  # White Green (22, 23)
        23: "U', F, U, L', Switch, L, U', F', U"  # Green White (23, 22)
    }
    print(switcher.get(argument))


# Solving Edges

def solveEdges(edge):
    solvededge = 0

    while solvededge == 0:
        if edge[0] == 0:  # if buffer == 0
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
        else:
            switchpos = 0
            found = 0

            while found == 0:  # look for position to be switched with
                if edge[0] == cor[switchpos]:
                    found = 1
                else:
                    switchpos += 1

            # switch
            printMoves(switchpos)
            if switchpos % 2 == 0:
                tmp1 = edge[0]
                tmp2 = edge[1]
                edge[0] = edge[switchpos]
                edge[1] = edge[switchpos + 1]
                edge[switchpos] = tmp1
                edge[switchpos + 1] = tmp2
            else:
                tmp1 = edge[0]
                tmp2 = edge[1]
                edge[0] = edge[switchpos]
                edge[1] = edge[switchpos - 1]
                edge[switchpos] = tmp1
                edge[switchpos - 1] = tmp2

            # check if solvededge
            solvedtmp = 1
            for x in range(24):
                if cor[x] != edge[x]:
                    solvedtmp = 0

            if solvedtmp == 1:
                solvededge = 1


def printCorners(argument):
    switcher = {
        0: "F, Switch, F'",  # Yellow Blue Orange (0, 1, 2)
        1: "",  # Blue Orange Yellow (1, 2, 0)
        2: "R2, Switch, R2",  # Orange Yellow blue (2, 0, 1)
        3: "F, R',  Switch, R, F'",  # Yellow Orange Green (3, 4, 5)
        4: "",  # Orange Green Yellow (4, 5, 3)
        5: "R2, D', Switch, D, R2",  # Green Yellow Orange (5, 3, 4)
        6: "",  # Yellow Green Red (6, 7, 8)
        7: "U', R', U, Switch U', R, U",  # Green Red Yellow (7, 8, 6)
        8: "R, D', Switch, D, R'",  # Red Yellow Green (8, 6, 7)
        9: "",  # Yellow Red Blue (9, 10, 11)
        10: "R', F, Switch, F', R", # Red Blue Yellow (10, 11, 9)
        11: "", # Blue Yellow Red (11, 9, 10)
        12: "", # White Blue Red (12, 13, 14)
        13: "D', R, Switch, R', D", # Blue Red White (13, 14, 12)
        14: "", # Red White Blue (14, 12, 13)
        15: "F', R', Switch, R, F", # White Orange Blue (15, 16, 17)
        16: "", # Orange Blue White (16, 17, 15)
        17: "D', Switch, D", # Blue White Orange (17, 15, 16)
        18: "", # White Green Orange (18, 19, 20)
        19: "F2, R', Switch, R, F2", # Green Orange White (19, 20, 18)
        20: "Switch", # Orange White Green (20, 18, 19)
        21: "D, F', Switch, F, D'", # White Red Green (21, 22, 23)
        22: "", # Red Green White (22, 23, 21)
        23: "", # Green White Red (23, 21, 22)
    }
    print(switcher.get(argument))


def solveCorner(corner):
    solvedCorner = 0

    while solvedCorner == 0:
        if corner[0] == 0:
            for x in range(24):
                if cor[x] != corner[x]:
                    printCorners(x)
                    tmp1 = corner[0]
                    tmp2 = corner[1]
                    tmp3 = corner[2]
                    corner[0] = corner[x]
                    corner[1] = corner[x + 1]
                    corner[2] = corner[x + 2]
                    corner[x] = tmp1
                    corner[x + 1] = tmp2
                    corner[x + 2] = tmp3
                    break
        elif corner[0] == 1:
            for x in range(1, 23):
                if cor[x] != corner[x]:  # and another argument
                    print("some shit needs to go here")
                    break
        elif corner[0] == 2:
            for x in range(2, 23):
                if cor[x] != corner[x]:  # and another argument
                    print("Some other shit goes here")
                    break

        switchPos = 0
        found = 0

        while found == 0:
            if corner[0] == cor[switchPos]:
                found = 1
            else:
                switchPos += 1

        printCorners(switchPos)
        if switchPos == 3 ^ 6 ^ 9 ^ 12 ^ 15 ^ 18 ^ 21:
            tmp1 = corner[0]
            tmp2 = corner[1]
            tmp3 = corner[2]
            corner[0] = corner[switchPos]
            corner[1] = corner[switchPos + 1]
            corner[2] = corner[switchPos + 2]
            corner[switchPos] = tmp1
            corner[switchPos + 1] = tmp2
            corner[switchPos + 2] = tmp3
        elif switchPos == 4 ^ 7 ^ 10 ^ 13 ^ 16 ^ 19 ^ 22:
            tmp1 = corner[0]
            tmp2 = corner[1]
            tmp3 = corner[2]
            corner[0] = corner[switchPos + 2]
            corner[1] = corner[switchPos]
            corner[2] = corner[switchPos + 1]
            corner[switchPos] = tmp3
            corner[switchPos + 1] = tmp1
            corner[switchPos + 2] = tmp2
        else:
            tmp1 = corner[0]
            tmp2 = corner[1]
            tmp3 = corner[2]
            corner[0] = corner[switchPos + 1]
            corner[1] = corner[switchPos + 2]
            corner[2] = corner[switchPos]
            corner[switchPos] = tmp2
            corner[switchPos + 1] = tmp3
            corner[switchPos + 2] = tmp1

        solvedtmp = 1
        for x in range(24):
            if cor[x] != corner[x]:
                solvedtmp = 0
            if solvedtmp == 1:
                solvedCorner = 1

        print(corner)
