# Rubik's cube solving bot
In this project I will try to eventually make a robot that:

Scans the cube
Output a sequence that will solve the cube
Preform the sequence of moves
This project however is still in development stage.

## Solving Methods
I've considered many methods of solving the cube. The way one would normally solve a cube requires a lot of intuition which is really hard for a computer. This is why the current method used is the "blind method". This method makes use of buffered switching. It is not efficient at all but gets the job done. Once the robot is fully functioning I will look into more efficient methods.

Position 0 is the buffer. The number in the position is read, and switched with the position of the value in the buffer. This repeats until all numbers are in the right place. If the buffer position is solved without the full sequence being solved it will switch with the next unsolved number and continue the switching.

### Example:
Number sequence: 20143
20143 -> 10243 -> 01243 -> 41203 -> 31204 -> 01234
The sequence to solve this set is: switch with position 2 then 1 then 3, 4 and finally 3.

## Development Progress
Currently writing the sorting/input code. Was able to sort the edges but parity became a problem. Also changed the input method to look at faces instead of pieces.
