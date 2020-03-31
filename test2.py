#Y = ['w', 'b', 'r', 'w', 'o', 'r', 'o', 'o']
#G = ['b', 'w', 'g', 'r', 'b', 'y', 'y', 'o']
#O = ['w', 'g', 'w', 'y', 'y', 'y', 'o', 'g']
#R = ['b', 'w', 'w', 'b', 'b', 'o', 'g', 'r']
#B = ['g', 'w', 'r', 'b', 'y', 'g', 'o', 'b']
#W = ['r', 'r', 'y', 'o', 'g', 'y', 'r', 'g']


# EDGES
def lookupEdge(arg1, arg2):
    if arg1 == 'y':
        if arg2 == 'o':
            return 0, 1
        elif arg2 == 'g':
            return 6, 7
        elif arg2 == 'r':
            return 2, 3
        elif arg2 == 'b':
            return 4, 5
    elif arg1 == 'w':
        if arg2 == 'o':
            return 16, 17
        elif arg2 == 'g':
            return 22, 23
        elif arg2 == 'r':
            return 18, 19
        elif arg2 == 'b':
            return 20, 21
    elif arg1 == 'g':
        if arg2 == 'o':
            return 11, 10
        elif arg2 == 'y':
            return 7, 6
        elif arg2 == 'r':
            return 12, 13
        elif arg2 == 'w':
            return 23, 22
    elif arg1 == 'b':
        if arg2 == 'o':
            return 8, 9
        elif arg2 == 'y':
            return 5, 4
        elif arg2 == 'r':
            return 15, 14
        elif arg2 == 'w':
            return 21, 20
    elif arg1 == 'r':
        if arg2 == 'b':
            return 14, 15
        elif arg2 == 'y':
            return 3, 2
        elif arg2 == 'g':
            return 3, 2
        elif arg2 == 'w':
            return 19, 18
    elif arg1 == 'o':
        if arg2 == 'b':
            return 9, 8
        elif arg2 == 'y':
            return 1, 0
        elif arg2 == 'g':
            return 10, 11
        elif arg2 == 'w':
            return 17, 16


def edgeAssign(Y, G, O, R, B, W):
    edge = [0 for x in range(24)]

    edge[0], edge[1] = lookupEdge(Y[3], O[1])
    edge[2], edge[3] = lookupEdge(Y[7], R[1])
    edge[4], edge[5] = lookupEdge(Y[1], B[1])
    edge[6], edge[7] = lookupEdge(Y[5], G[1])

    edge[8], edge[9] = lookupEdge(B[7], O[3])
    edge[10], edge[11] = lookupEdge(O[7], G[3])
    edge[12], edge[13] = lookupEdge(G[7], R[3])
    edge[14], edge[15] = lookupEdge(R[7], B[3])

    edge[16], edge[17] = lookupEdge(W[3], O[5])
    edge[18], edge[19] = lookupEdge(W[7], R[5])
    edge[20], edge[21] = lookupEdge(W[5], B[5])
    edge[22], edge[23] = lookupEdge(W[1], G[5])

    print(edge)
    return edge


# Corners
def lookupCorner(arg1, arg2):
    if arg1 == 'y':
        if arg2 == 'b':
            return 0, 1, 2
        elif arg2 == 'o':
            return 3, 4, 5
        elif arg2 == 'g':
            return 6, 7, 8
        elif arg2 == 'r':
            return 9, 10, 11
    elif arg1 == 'w':
        if arg2 == 'b':
            return 21, 23, 22
        elif arg2 == 'o':
            return 15, 16, 17
        elif arg2 == 'g':
            return 18, 19, 20
        elif arg2 == 'r':
            return 21, 22, 23
    elif arg1 == 'g':
        if arg2 == 'y':
            return 5, 3, 4
        elif arg2 == 'o':
            return 17, 16, 15
        elif arg2 == 'w':
            return 19, 18, 20
        elif arg2 == 'r':
            return 7, 8, 6
    elif arg1 == 'b':
        if arg2 == 'y':
            return 11, 9, 10
        elif arg2 == 'r':
            return 23, 22, 21
        elif arg2 == 'w':
            return 13, 12, 14
        elif arg2 == 'o':
            return 1, 2, 0
    elif arg1 == 'r':
        if arg2 == 'y':
            return 8, 6, 7
        elif arg2 == 'g':
            return 20, 19, 18
        elif arg2 == 'w':
            return 22, 21, 23
        elif arg2 == 'b':
            return 10, 11, 9
    elif arg1 == 'o':
        if arg2 == 'y':
            return 2, 0, 1
        elif arg2 == 'b':
            return 14, 13, 12
        elif arg2 == 'w':
            return 16, 15, 17
        elif arg2 == 'g':
            return 5, 4, 3

def cornerAssign(Y, G, O, R, B, W):
    corner = [0 for x in range(24)]

    corner[0], corner[1], corner[2] = lookupCorner(Y[2], B[0])
    corner[3], corner[4], corner[5] = lookupCorner(Y[4], O[0])
    corner[6], corner[7], corner[8] = lookupCorner(Y[6], G[0])
    corner[9], corner[10], corner[11] = lookupCorner(Y[0], R[0])

    corner[12], corner[13], corner[14] = lookupCorner(W[4], O[4])
    corner[15], corner[16], corner[17] = lookupCorner(W[2], G[4])
    corner[18], corner[19], corner[20] = lookupCorner(W[0], R[4])
    corner[20], corner[21], corner[23] = lookupCorner(W[6], B[4])

    print(corner)
    return corner