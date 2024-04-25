import time

number_of_columns = 20
number_of_rows = 10
empty_marker = " "
filled_marker = "X"

game_board = [[empty_marker for _ in range(number_of_columns)] for _ in range(number_of_rows)]

# Add 'x' in row 1 and 8
for col in range(number_of_columns):
    game_board[1][col] = filled_marker
    game_board[8][col] = filled_marker

# Add 'x' in column 3 and 15
for row in range(number_of_rows):
    game_board[row][3] = filled_marker
    game_board[row][15] = filled_marker

def print_game_board(game_board):
    for row in game_board:
        print(''.join(row))

# Startpunkte und die Richtungen
start_points = [(5, 5), (5, 10)]
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
            time.sleep(0.5)







