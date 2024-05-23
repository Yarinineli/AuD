import time
import random

number_of_columns = 76
number_of_rows = 30
empty_marker = " "
filled_marker = "x"

def print_game_board(game_board):
    for row in game_board:
        print(''.join(row))
    print("\n")

def convert_file_to_field(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

# Beispiel-Spielfeld in "field.txt" lesen
game_board = convert_file_to_field("field.txt")

# Debugging-Ausgaben
print("Spielfeldgröße:", len(game_board), "x", len(game_board[0]))

# Startpunkte und die Richtungen
start_points = [(len(game_board) // 2, len(game_board[0]) // 2)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Prüfplan
points_to_check = start_points[:]

# Funktion zur Überprüfung, ob die Position innerhalb der Spielfeldgrenzen liegt
def is_within_bounds(ni, nj):
    return 0 <= ni < len(game_board) and 0 <= nj < len(game_board[0])

while points_to_check:
    point = points_to_check.pop(0)
    print("Checking", point[0], point[1])  # Debugging-Ausgabe
    for direction in directions:
        ni, nj = point[0] + direction[0], point[1] + direction[1]
        print("Next index:", ni, nj)  # Debugging-Ausgabe
        # Überprüfen Sie, ob die neue Position innerhalb des Spielbretts liegt
        if is_within_bounds(ni, nj):
            # Überprüfen Sie, ob die Position nicht bereits gefüllt ist
            if game_board[ni][nj] != filled_marker:
                # Füllen Sie die Position
                game_board[ni][nj] = filled_marker
                # Fügen Sie den neuen Punkt zur Liste der zu überprüfenden Punkte hinzu
                points_to_check.append((ni, nj))
                print_game_board(game_board)
        else:
            print("Index out of bounds:", ni, nj)  # Debugging-Ausgabe
            print("Current game board size:", len(game_board), "x", len(game_board[0]))  # Debugging-Ausgabe
