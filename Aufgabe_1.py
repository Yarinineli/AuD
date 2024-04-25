number_of_columns = 20
number_of_rows = 10
empty_marker = " "
filled_marker = "X"

game_board = [['' for _ in range(number_of_columns)] for _ in range(number_of_rows)]

# Add 'x' in row 1 and 8
for col in range(number_of_columns):
    game_board[1][col] = filled_marker
    game_board[8][col] = filled_marker

# Add 'x' in column 3 and 15
for row in range(number_of_rows):
    game_board[row][3] = filled_marker
    game_board[row][15] = filled_marker

import matplotlib.pyplot as plt

# Convert game board to numerical values for plotting
game_board_plot = [[1 if cell == filled_marker else 0 for cell in row] for row in game_board]

plt.imshow(game_board_plot, cmap='binary')
plt.show()