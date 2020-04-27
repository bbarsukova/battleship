from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

all_ships = []
for ships in range(2):
  ship = [0,0]
  ship[0] = random_row(board)
  ship[1]= random_col(board)

  if ships == 2:
    if ship[0] == all_ships[0][0] and ship[1] == all_ships[0][1]:
      ship[0] = random_row(board)
      ship[1] = random_col(board)
  all_ships.append(ship)

broken_boat = 0
for turn in range(4):
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if (guess_row == all_ships[0][0] and guess_col ==  all_ships[0][1]) or (guess_row == all_ships[1][0] and guess_col ==  all_ships[1][1]):
    print "Congratulations! You sank my battleship!"
    broken_boat += 1
    if broken_boat == 2:
      break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
    if turn == 3:
      print "Game Over"

      board[guess_row][guess_col] = "X"
    print_board(board)
  print (turn + 1)
