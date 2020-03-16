yellowArray = list()
greenArray = list()
redArray = list()
orangeArray = list()
blueArray = list()
whiteArray = list()


print("Welcome to the rubik's solving bot!")
print("Hold your cube with the yellow center on top and the green facing you.")
print("              -----------")
print("             | 1 | 2 | 3 |")
print("             | 8 | Y | 4 |")
print("             | 7 | 6 | 5 |")
print(" -----------  -----------  -----------  -----------")
print("| 1 | 2 | 3 || 1 | 2 | 3 || 1 | 2 | 3 || 1 | 2 | 3 |")
print("| 8 | R | 4 || 8 | G | 4 || 8 | O | 4 || 8 | B | 4 |")
print("| 7 | 6 | 5 || 7 | 6 | 5 || 7 | 6 | 5 || 7 | 6 | 5 |")
print(" -----------  -----------  -----------  -----------")
print("             | 1 | 2 | 3 |")
print("             | 8 | W | 4 |")
print("             | 7 | 6 | 5 |")
print("              -----------")
print("Imagine the cube folded out like in the diagram above.")

while False:
    inp = input("enter the yellow faces separated by a comma:   ")
    yellowArray = inp.split(' ')

    inp = input("enter the green faces separated by a comma:    ")
    greenArray = inp.split(' ')

    inp = input("enter the red faces separated by a comma:      ")
    redArray = inp.split(' ')

    inp = input("enter the orange faces separated by a comma:   ")
    orangeArray = inp.split(' ')

    inp = input("enter the blue faces separated by a comma:     ")
    blueArray = inp.split(' ')

    inp = input("enter the white faces separated by a comma:    ")
    whiteArray = inp.split(' ')

    print("              -----------")
    print(f"             | {yellowArray[0]} | {yellowArray[1]} | {yellowArray[2]} |")
    print(f"             | {yellowArray[7]} | Y | {yellowArray[3]} |")
    print(f"             | {yellowArray[6]} | {yellowArray[5]} | {yellowArray[4]} |")
    print(" -----------  -----------  -----------  -----------")
    print(f"| {redArray[0]} | {redArray[1]} | {redArray[2]} || {greenArray[0]} | {greenArray[1]} | {greenArray[2]} || {orangeArray[0]} | {orangeArray[1]} | {orangeArray[2]} || {blueArray[0]} | {blueArray[1]} | {blueArray[2]} |")
    print(f"| {redArray[7]} | R | {redArray[3]} || {greenArray[7]} | G | {greenArray[3]} || {orangeArray[7]} | O | {orangeArray[3]} || {blueArray[7]} | b | {blueArray[3]} |")
    print(f"| {redArray[6]} | {redArray[5]} | {redArray[4]} || {greenArray[6]} | {greenArray[5]} | {greenArray[4]} || {orangeArray[6]} | {orangeArray[5]} | {orangeArray[4]} || {blueArray[6]} | {blueArray[5]} | {blueArray[4]} |")
    print(" -----------  -----------  -----------  -----------")
    print(f"             | {whiteArray[0]} | {whiteArray[1]} | {whiteArray[2]} |")
    print(f"             | {whiteArray[7]} | W | {whiteArray[3]} |")
    print(f"             | {whiteArray[6]} | {whiteArray[5]} | {whiteArray[4]} |")
    print("              -----------")

    inp = input('is this correct? (y/n) ')
    if inp == 'y' :
        break

print('the solve will be here')

edgeArray = list()
translate_map = {'y': {'o': (0,1), 'r': (2,3), 'b': (4,5), 'g': (6,7)}}

# ''
# _map['y'][3]['r']['g']
# _map[array][index][value][

# comp = pos_map['y'][3]['comp']
# _map['y'][3][ values['y'][3] ][ values[comp][1] ]

values = {
    'y': [],
    'o': [],
    # ...
}

pos_map = {
    'y': {
        3: {
            'comp': 'o',
            'val': (0, 1)
        }
    },

}

val_map = {
    'y': { # Yellow Array
        1: {

        },
        3: {
            'y': {
                'o': (0, 1),
                'r': (2, 3),
                'b': (4, 5),
                'g': (6, 7),
            },
            'o': {
                'y': (1, 0),
                'b': (9, 8),
                'w': (17, 16),
                'g': (10, 11),
            },
            'g': {},
            'r': {},
            'b': {},
            'w': {},
        },
        5: {

        },
        7: {

        }
    }
}

# Postion 1 (yellow orange)
if yellowArray[3] == 'y' :
    if orangeArray[1] == 'o':
        edgeArray[0] = 0
        edgeArray[1] = 1
    elif orangeArray[1] == 'r':
        edgeArray[0] = 2
        edgeArray[1] = 3
    elif orangeArray[1] == 'b':
        edgeArray[0] = 4
        edgeArray[1] = 5
    elif orangeArray[1] == 'g':
        edgeArray[0] = 6
        edgeArray[1] = 7
elif yellowArray[3] == 'o':
    if orangeArray[1] == 'y' :
        edgeArray[0] = 1
        edgeArray[1] = 0
    elif orangeArray[1] == 'b':
        edgeArray[0] = 9
        edgeArray[1] = 8
    elif orangeArray[1] == 'w':
        edgeArray[0] = 17
        edgeArray[1] = 16
    elif orangeArray[1] == 'g':
        edgeArray[0] = 10
        edgeArray[1] = 11
elif yellowArray[3] == 'g':
    if orangeArray[1] == 'y' :
        edgeArray[0] = 6
        edgeArray[1] = 7
    elif orangeArray[1] == 'r':
        edgeArray[0] = 12
        edgeArray[1] = 13
    elif orangeArray[1] == 'w':
        edgeArray[0] = 23
        edgeArray[1] = 22
    elif orangeArray[1] == 'o':
        edgeArray[0] = 11
        edgeArray[1] = 10
elif yellowArray[3] == 'r':
    if orangeArray[1] == 'y' :
        edgeArray[0] = 3
        edgeArray[1] = 2
    elif orangeArray[1] == 'g':
        edgeArray[0] = 13
        edgeArray[1] = 12
    elif orangeArray[1] == 'w':
        edgeArray[0] = 19
        edgeArray[1] = 18
    elif orangeArray[1] == 'b':
        edgeArray[0] = 14
        edgeArray[1] = 15
elif yellowArray[3] == 'b':
    if orangeArray[1] == 'y' :
        edgeArray[0] = 5
        edgeArray[1] = 4
    elif orangeArray[1] == 'r':
        edgeArray[0] = 15
        edgeArray[1] = 14
    elif orangeArray[1] == 'w':
        edgeArray[0] = 21
        edgeArray[1] = 20
    elif orangeArray[1] == 'o':
        edgeArray[0] = 8
        edgeArray[1] = 9
elif yellowArray[3] == 'w':
    if orangeArray[1] == 'o' :
        edgeArray[0] = 5
        edgeArray[1] = 4
    elif orangeArray[1] == 'r':
        edgeArray[0] = 15
        edgeArray[1] = 14
    elif orangeArray[1] == 'b':
        edgeArray[0] = 21
        edgeArray[1] = 20
    elif orangeArray[1] == 'g':
        edgeArray[0] = 8
        edgeArray[1] = 9

# Positon 2 (yellow green)
if yellowArray[5] == 'y' :
    if greenArray[1] == 'o':
        edgeArray[2] = 0
        edgeArray[3] = 1
    elif greenArray[1] == 'r':
        edgeArray[2] = 2
        edgeArray[3] = 3
    elif greenArray[1] == 'b':
        edgeArray[2] = 4
        edgeArray[3] = 5
    elif greenArray[1] == 'g':
        edgeArray[2] = 6
        edgeArray[3] = 7
elif yellowArray[5] == 'o':
    if greenArray[1] == 'y' :
        edgeArray[2] = 1
        edgeArray[3] = 0
    elif greenArray[1] == 'b':
        edgeArray[2] = 9
        edgeArray[3] = 8
    elif greenArray[1] == 'w':
        edgeArray[2] = 17
        edgeArray[3] = 16
    elif greenArray[1] == 'g':
        edgeArray[2] = 10
        edgeArray[3] = 11
elif yellowArray[5] == 'g':
    if greenArray[1] == 'y' :
        edgeArray[2] = 6
        edgeArray[3] = 7
    elif greenArray[1] == 'r':
        edgeArray[2] = 12
        edgeArray[3] = 13
    elif greenArray[1] == 'w':
        edgeArray[2] = 23
        edgeArray[3] = 22
    elif greenArray[1] == 'o':
        edgeArray[2] = 11
        edgeArray[3] = 10
elif yellowArray[5] == 'r':
    if greenArray[1] == 'y' :
        edgeArray[2] = 3
        edgeArray[3] = 2
    elif greenArray[1] == 'g':
        edgeArray[2] = 13
        edgeArray[3] = 12
    elif greenArray[1] == 'w':
        edgeArray[2] = 19
        edgeArray[3] = 18
    elif greenArray[1] == 'b':
        edgeArray[2] = 14
        edgeArray[3] = 15
elif yellowArray[5] == 'b':
    if greenArray[1] == 'y' :
        edgeArray[2] = 5
        edgeArray[3] = 4
    elif greenArray[1] == 'r':
        edgeArray[2] = 15
        edgeArray[3] = 14
    elif greenArray[1] == 'w':
        edgeArray[2] = 21
        edgeArray[3] = 20
    elif greenArray[1] == 'o':
        edgeArray[2] = 8
        edgeArray[3] = 9

