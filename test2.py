Y = ['b', 'w', 'r', 'o']
G = ['w', 'r', 'g', 'o']
O = ['g', 'y', 'y', 'g']
R = ['w', 'b', 'o', 'r']
B = ['w', 'b', 'g', 'b']
W = ['r', 'o', 'y', 'g']

def lookup(arg1, arg2):
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

edge = [0 for x in range(24)]

edge[0], edge[1] = lookup(Y[1], O[0])
edge[2], edge[3] = lookup(Y[3], R[0])
edge[4], edge[5] = lookup(Y[0], B[0])
edge[6], edge[7] = lookup(Y[2], G[0])

edge[8], edge[9] = lookup(B[3], O[1])
edge[10], edge[11] = lookup(O[3], G[1])
edge[12], edge[13] = lookup(G[3], R[1])
edge[14], edge[15] = lookup(R[3], B[1])

edge[16], edge[17] = lookup(W[1], O[2])
edge[18], edge[19] = lookup(W[3], R[2])
edge[20], edge[21] = lookup(W[2], B[2])
edge[22], edge[23] = lookup(W[0], G[2])

print(edge)
