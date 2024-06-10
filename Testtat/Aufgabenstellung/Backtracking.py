import os

# from Seminar_2 import convert_file_to_field, am liebsten würde ich gerne das Modul aus meinem Verzeichnis importieren.
############################################################################
# a)
def convert_file_to_field(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"Die Datei {filename} wurde nicht gefunden.")
    
    with open(filename, 'r') as file:
        # Strip nimmt mir die Leerzeichen weg
        return [list(line[:-1]) for line in file]

def print_game_board(game_board):
    for row in game_board:
        print(''.join(row))
    print("\n")

############################################################################
# b)

def is_free(game_board, row_number, column_number):
    if 0 <= row_number < len(game_board) and 0 <= column_number < len(game_board[0]):
        return game_board[row_number][column_number] != 'x'
    else:
        return False
    

############################################################################
# c)

def is_escaped(game_board, row_number, column_number):
    print(f"Checking if escaped at position ({row_number}, {column_number})")
    if 0 <= row_number < len(game_board) and 0 <= column_number < len(game_board[0]):
        return game_board[row_number][column_number] == 'E'
    else:
        return False

def find_escape(game_board, row_number, column_number, route=()):
    #print(f"Finding escape from position ({row_number}, {column_number})")
    if game_board[row_number][column_number] == 'E':
        return route + ((row_number, column_number),)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    shortest_route = None
    for dr, dc in directions:
        new_row, new_col = row_number + dr, column_number + dc
        new_position = (new_row, new_col)
        if is_free(game_board, new_row, new_col) and new_position not in route:
            new_route = find_escape(game_board, new_row, new_col, route + (new_position,))
            if new_route and (not shortest_route or len(new_route) < len(shortest_route)):
                shortest_route = new_route

    return shortest_route

try:
    game_board = convert_file_to_field('field3.txt')
except FileNotFoundError as e:
    print(e)
    game_board = []

if game_board:
    print("Game board loaded successfully")
    escape_route = find_escape(game_board, 1, 1)
    if escape_route:
        print("Escape route found:", escape_route)
    else:
        print("No escape route found")