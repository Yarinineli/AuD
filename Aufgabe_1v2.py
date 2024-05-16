import time
import random


# Define the function to convert the file to a game board field
def convert_file_to_field(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()
    
    # Initialize an empty game board
    game_board = []
    
    # Iterate over each line in the file
    for line in lines:
        # Remove leading and trailing whitespaces and split the line into a list of values
        row = line.strip().split()
        # Append the row to the game board
        game_board.append(row)
    
    # Return the game board
    return game_board

number_of_columns = 70
number_of_rows = 20
empty_marker = " "
filled_marker = "X"

game_board = [[empty_marker for _ in range(number_of_columns)] for _ in range(number_of_rows)]

# Add 'x' in row 1 and 8
for col in range(number_of_columns):
    game_board[1][col] = filled_marker
    game_board[-3][col] = filled_marker

# Add 'x' in column 3 and 15
for row in range(number_of_rows):
    game_board[row][3] = filled_marker
    game_board[row][-3] = filled_marker

def print_game_board(game_board):
    for row in game_board:
        print(''.join(row))

# Startpunkte und die Richtungen
start_points = []
while True:
    start_point = (random.randint(0, number_of_rows-1), random.randint(0, number_of_columns-1))
    if game_board[start_point[0]][start_point[1]] == empty_marker:
        start_points.append(start_point)
        break
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Startpunkte füllen
for point in start_points:
    game_board[point[0]][point[1]] = filled_marker

# Prüfplan
points_to_check = start_points[:]

while points_to_check:
    point = points_to_check.pop(0)
    for direction in directions:
        ni, nj = point[0] + direction[0], point[1] + direction[1]
        # Überprüfen Sie, ob die neue Position innerhalb des Spielbretts liegt und ob sie leer ist
        if 0 <= ni < len(game_board) and 0 <= nj < len(game_board[0]) and game_board[ni][nj] != filled_marker:
            # Füllen Sie die Position
            game_board[ni][nj] = filled_marker
            # Fügen Sie den neuen Punkt zur Liste der zu überprüfenden Punkte hinzu
            points_to_check.append((ni, nj))
            print_game_board(game_board)
            