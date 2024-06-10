import os

# from Seminar_2 import convert_file_to_field, am liebsten würde ich gerne das Modul aus meinem Verzeichnis importieren.
############################################################################
# a)
def convert_file_to_field(filename):
    # Ich überprüfe, ob die Datei existiert.
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"Die Datei {filename} wurde nicht gefunden.")
    
    # Ich öffne die Datei und lese das Spielbrett ein.
    with open(filename, 'r') as file:
        # Strip würde mir die Leerzeichen weg nehmen, daher folgendes: 
        game_board = [list(line[:-1]) for line in file]
    
    # Wenn die Zelle 'NaN' ist, ersetze ich sie durch ein Leerzeichen.
    for row in game_board:
        for i in range(len(row)):
            if row[i] == 'NaN':
                row[i] = ' '
                
    
    return game_board

def print_game_board(game_board):
    for row in game_board:
        print(''.join(row))
    print("\n")

############################################################################
# b)


# Ich überprüfe, ob die gegebene Position innerhalb des Spielbretts liegt und ob sie frei ist.
def is_free(game_board, row_number, column_number):
    if 0 <= row_number < len(game_board) and 0 <= column_number < len(game_board[0]):
        return game_board[row_number][column_number] != 'x'
    else:
        return False
    

############################################################################
# c)

# Ich überprüfe, ob die gegebene Position innerhalb des Spielbretts liegt und ob sie den Ausgang darstellt.
def is_escaped(game_board, row_number, column_number):
    print(f"Checking if escaped at position ({row_number}, {column_number})")
    if 0 <= row_number < len(game_board) and 0 <= column_number < len(game_board[0]):
        return game_board[row_number][column_number] == 'E'
    else:
        return False

############################################################################
# d)
def find_escape(game_board, row_number, column_number, visited=None, route=None, depth=0):
    if route is None:
        route = ()
    if visited is None:
        visited = set()

    print(f"Depth {depth}: Visiting position ({row_number}, {column_number})")

    if game_board[row_number][column_number] == 'E':
        print(f"Depth {depth}: Escape found at position ({row_number}, {column_number})")
        return route + ((row_number, column_number),)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    shortest_route = None
    for dr, dc in directions:
        new_row, new_col = row_number + dr, column_number + dc
        new_position = (new_row, new_col)
        if is_free(game_board, new_row, new_col) and new_position not in visited:
            print(f"Depth {depth}: Moving to position ({new_row}, {new_col})")
            visited.add(new_position)
            new_route = find_escape(game_board, new_row, new_col, visited, route + (new_position,), depth + 1)
            if new_route and (not shortest_route or len(new_route) < len(shortest_route)):
                shortest_route = new_route

    return shortest_route

try:
    game_board = convert_file_to_field('field2.txt')
except FileNotFoundError as e:
    print(e)
    game_board = []

if game_board:
    print("Game board loaded successfully")
    escape_route = find_escape(game_board, 1, 1)
    if escape_route:
        print("Escape route found:", escape_route)
        for row in range(len(game_board)):
            for col in range(len(game_board[0])):
                if (row, col) in escape_route:
                    print('#', end='')
                else:
                    print(game_board[row][col], end='')
            print()
    else:
        print("No escape route found")
else:
    print("Game board could not be loaded.")
