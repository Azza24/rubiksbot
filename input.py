from test2 import cornerAssign, edgeAssign
from solve import solveEdges, solveCorner

yellowArray = ['w', 'b', 'r', 'w', 'o', 'r', 'o', 'o']
greenArray = ['b', 'w', 'g', 'r', 'b', 'y', 'y', 'o']
redArray = ['w', 'g', 'w', 'y', 'y', 'y', 'o', 'g']
orangeArray = ['b', 'w', 'w', 'b', 'b', 'o', 'g', 'r']
blueArray = ['g', 'w', 'r', 'b', 'y', 'g', 'o', 'b']
whiteArray = ['r', 'r', 'y', 'o', 'g', 'y', 'r', 'g']


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

while False: # Change this to true when testing the whole thing
    inp = input("enter the yellow faces separated by a space:   ")
    yellowArray = inp.split(' ')

    inp = input("enter the green faces separated by a space:    ")
    greenArray = inp.split(' ')

    inp = input("enter the red faces separated by a space:      ")
    redArray = inp.split(' ')

    inp = input("enter the orange faces separated by a space:   ")
    orangeArray = inp.split(' ')

    inp = input("enter the blue faces separated by a space:     ")
    blueArray = inp.split(' ')

    inp = input("enter the white faces separated by a space:    ")
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


edges = [0]*24
edges = edgeAssign(yellowArray, greenArray, redArray, orangeArray, blueArray, whiteArray)

corners = [0]*24
corners = cornerAssign(yellowArray, greenArray, redArray, orangeArray, blueArray, whiteArray)

solveEdges(edges)
solveCorner(corners)

