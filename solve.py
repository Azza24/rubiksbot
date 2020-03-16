cor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
edge = [23, 22, 17, 16, 20, 21, 1, 0, 12, 13, 6, 7, 5, 4, 2, 3, 9, 8, 19, 18, 14, 15, 11, 10]

def printMoves(argument):
    switcher = {
        0: "Nothing?", # Yellow orange (0, 1) Solved
        1: "Flip buffer / don't know how yet lel",  # Orange Yellow (1, 0)
        2: "Switch", # Yellow red (2, 3)
        3: "L, U', F, U, Switch, U', F', U, L'", # Red yellow (3, 2)
        4: "Imma do this tomorrow lel",
        5: "some moves here",
        6: "R2, R, R2, Switch, R2, R' R2", # Yellow green (6, 7)
    }
    print(switcher.get(argument))
