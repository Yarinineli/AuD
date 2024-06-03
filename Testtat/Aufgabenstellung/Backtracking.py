# from Seminar_2 import convert_file_to_field, am liebsten würde ich gerne das Modul aus meinem Verzeichnis importieren.
############################################################################
# a)
def convert_file_to_field(filename):
    with open(filename, 'r') as file:
        #Strip nimmt mir die Leerzeichen weg
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
    if 0 <= row_number < len(game_board) and 0 <= column_number < len(game_board[0]):
        return game_board[row_number][column_number] == 'E'
    else:
        return False
    

############################################################################
# d)
def find_escape(game_board, row_number, column_number, route=()):
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
game_board = convert_file_to_field('field3.txt')

escape_route = find_escape(game_board, 1, 1)

if escape_route:
    for row in range(len(game_board)):
        for col in range(len(game_board[0])):
            if (row, col) in escape_route:
                print('#', end='')
            else:
                print(game_board[row][col], end='')
        print()
else:
    print("No escape route found.")
