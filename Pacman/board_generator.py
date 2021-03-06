import random

board = [
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 2, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 6, 2, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 6, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 2, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 2, 2, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 2, 3],
    [3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 2, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 2, 3],
    [3, 3, 2, 2, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 3, 2, 3, 2, 2, 3],
    [3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3],  # Middle Lane
    [3, 3, 3, 3, 3, 3, 2, 3, 3, 1, 3, 1, 1, 4, 1, 1, 1, 3, 1, 3, 3, 2, 3, 3, 3, 3, 3, 3],
    [3, 3, 1, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3, 3, 3],
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 2, 3],
    [3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 2, 3, 3, 3, 3, 3, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 2, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 2, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 6, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 2, 1, 1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 6, 3],
    [3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 2, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 2, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3],
    [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 2, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]

# predefine the location that we want to ignore
visited = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12],
           [0, 13],
           [0, 14], [0, 15], [0, 16], [0, 17], [0, 18], [0, 19], [0, 20], [0, 21], [0, 22], [0, 23], [0, 24], [0, 25],
           [0, 26], [0, 27],
           [30, 0], [30, 1], [30, 2], [30, 3], [30, 4], [30, 5], [30, 6], [30, 7], [30, 8], [30, 9], [30, 10], [30, 11],
           [30, 12], [30, 13],
           [30, 14], [30, 15], [30, 16], [30, 17], [30, 18], [30, 19], [30, 20], [30, 21], [30, 22], [30, 23], [30, 24],
           [30, 25], [30, 26], [30, 27],
           [1, 0], [1, 27], [2, 0], [2, 27], [3, 0], [3, 27], [4, 0], [4, 27], [5, 0], [5, 27], [6, 0], [6, 27], [7, 0],
           [7, 27], [8, 0], [8, 27],
           [9, 0], [9, 27], [10, 0], [10, 27], [11, 0], [11, 27], [12, 0], [12, 27], [13, 0], [13, 27], [14, 0],
           [14, 27], [15, 0], [15, 27], [16, 0], [16, 27],
           [17, 0], [17, 27], [18, 0], [18, 27], [19, 0], [19, 27], [20, 0], [20, 27], [21, 0], [21, 27], [22, 0],
           [22, 27], [23, 0], [23, 27], [24, 0], [24, 27],
           [25, 0], [25, 27], [26, 0], [26, 27], [27, 0], [27, 27], [28, 0], [28, 27], [29, 0], [29, 27],[23, 13], [23, 14],
[3, 1], [3, 26], [23, 1], [23, 26],[14, 12], [14, 13], [14, 14], [15, 13],
           ]
x = 1
y = 1
start_position = [x, y]
stack = []
grid = []
stack.append([x, y])
visited.append(start_position)

# define the grid
for i, row in enumerate(board):
    for j, block in enumerate(row):
        if [i, j] not in visited:
            grid.append([i, j])

while len(stack) > 0:
    move = []
    if [x + 2, y] not in visited and [x + 2, y] in grid:  # prevent the calculation go off the screen
        move.append("right")
    if [x - 2, y] not in visited and [x - 2, y] in grid:
        move.append("left")
    if [x, y + 2] not in visited and [x, y + 2] in grid:
        move.append("down")
    if [x, y - 2] not in visited and [x, y - 2] in grid:
        move.append("up")

    if len(move) > 0:
        random_move = random.choice(move)  # pick a random neighboring cell that hasn't been visited
        if random_move == "right":
            x += 2
            board[x-1][y] = 2  # Remove the wall
            stack.append([x, y])  # add the current cell to the stack
            visited.append([x, y])  # make the chosen cell the current cell and mark it visited

        elif random_move == "left":
            x -= 2
            board[x+1][y] = 2  # Remove the wall
            stack.append([x, y])  # add the current cell to the stack
            visited.append([x, y])  # make the chosen cell the current cell and mark it visited

        elif random_move == "down":
            y += 2
            board[x][y-1] = 2  # Remove the wall
            stack.append([x, y])  # add the current cell to the stack
            visited.append([x, y])  # make the chosen cell the current cell and mark it visited

        elif random_move == "up":
            y -= 2
            board[x][y+1] = 2  # Remove the wall
            stack.append([x, y])  # add the current cell to the stack
            visited.append([x, y])  # make the chosedn cell the current cell and mark it visited
    else:
        x, y = stack.pop()  # if the current cell has no unvisited neighbors, take the top cell from the stack and
        # make it current cell

random_board = board


