HorFrame = "+---+---+---+---+---+---+---+\n"
EmptyFrame = "|   |   |   |   |   |   |   |\n"
Header = "  1   2   3   4   5   6   7  \n"
LE = "| "
RE = " |\n"
CE = " | "
rows = ["a", "b", "c", "d", "e", "f"]
columns = ['1', '2', '3', '4', '5', '6', '7']
full_columns = []
total_dropped = 0

def show_board():
  print("_______________________________\n")
  print()
  print("The current player is " + CurrPlayer[0] + ". Please select a column to drop an " + CurrPlayer[1] + ".\n")
  print(Header + RowF + RowE + RowD + RowC + RowB + RowA + HorFrame)
  print()

def update_rows():
  global CenterA
  global CenterB
  global CenterC
  global CenterD
  global CenterE
  global CenterF
  global RowA
  global RowB
  global RowC
  global RowD
  global RowE
  global RowF
  CenterA = LE + Spaces['a1'] + CE + Spaces['a2'] + CE + Spaces['a3'] + CE + Spaces['a4'] + CE + Spaces['a5'] + CE + Spaces['a6'] + CE + Spaces['a7'] + RE
  CenterB = LE + Spaces['b1'] + CE + Spaces['b2'] + CE + Spaces['b3'] + CE + Spaces['b4'] + CE + Spaces['b5'] + CE + Spaces['b6'] + CE + Spaces['b7'] + RE
  CenterC = LE + Spaces['c1'] + CE + Spaces['c2'] + CE + Spaces['c3'] + CE + Spaces['c4'] + CE + Spaces['c5'] + CE + Spaces['c6'] + CE + Spaces['c7'] + RE
  CenterD = LE + Spaces['d1'] + CE + Spaces['d2'] + CE + Spaces['d3'] + CE + Spaces['d4'] + CE + Spaces['d5'] + CE + Spaces['d6'] + CE + Spaces['d7'] + RE
  CenterE = LE + Spaces['e1'] + CE + Spaces['e2'] + CE + Spaces['e3'] + CE + Spaces['e4'] + CE + Spaces['e5'] + CE + Spaces['e6'] + CE + Spaces['e7'] + RE
  CenterF = LE + Spaces['f1'] + CE + Spaces['f2'] + CE + Spaces['f3'] + CE + Spaces['f4'] + CE + Spaces['f5'] + CE + Spaces['f6'] + CE + Spaces['f7'] + RE
  RowA = HorFrame + CenterA
  RowB = HorFrame + CenterB
  RowC = HorFrame + CenterC
  RowD = HorFrame + CenterD
  RowE = HorFrame + CenterE
  RowF = HorFrame + CenterF
def switch_player(CurrPlayer):
  if CurrPlayer == Player1:
    return Player2
  elif CurrPlayer == Player2:
    return Player1

def check_piece_match(pieced, piece):
  if Spaces[pieced] == piece:
    return True
  else:
    return False

def check_and_drop(col):
  while col not in columns:
    print("The column you gave is not recognized, please try again, entering a column from 1 to 7.")
    col = get_col()
  while col in full_columns:
    print("The column you selected is full. Please choose a different column")
    col = get_col()
  for row in rows:
    global pieced
    pieced = str(row) + str(col)
    if Spaces[pieced] == " ":
      Spaces[pieced] = CurrPlayer[1]
      if row == 'f':
        full_columns.append(col)
      return
def check_winner():
  for row in rows:
    for col in columns:
      #Horizontal
      if col in "1234":
        tpieced1 = str(row) + str(col)
        tpieced2 = str(row) + str(int(col) + 1)
        tpieced3 = str(row) + str(int(col) + 2)
        tpieced4 = str(row) + str(int(col) + 3)
        piece = Spaces[tpieced1]
        if Spaces[tpieced1] == piece and Spaces[tpieced2] == piece and Spaces[tpieced3] == piece and Spaces[tpieced4] == piece and piece != " ":
          declare_winner()
          return
      #Vertical
      if row in "abc":
        if row == 'a':
          rowdes = 0
        elif row == 'b':
          rowdes = 1
        elif row == 'c':
          rowdes = 2
        tpieced1 = str(rows[rowdes]) + str(col)
        tpieced2 = str(rows[rowdes + 1]) + str(col)
        tpieced3 = str(rows[rowdes + 2]) + str(col)
        tpieced4 = str(rows[rowdes + 3]) + str(col)
        piece = Spaces[tpieced1]
        if Spaces[tpieced1] == piece and Spaces[tpieced2] == piece and Spaces[tpieced3] == piece and Spaces[tpieced4] == piece and piece != " ":
          declare_winner()
          return
      #Diagonal Up
      if col in "1234" and row in "abc":
        if row == 'a':
              rowdes = 0
        elif row == 'b':
              rowdes = 1
        elif row == 'c':
              rowdes = 2
        tpieced1 = str(rows[rowdes]) + str(col)
        tpieced2 = str(rows[rowdes + 1]) + str(int(col) + 1)
        tpieced3 = str(rows[rowdes + 2]) + str(int(col) + 2)
        tpieced4 = str(rows[rowdes + 3]) + str(int(col) + 3)
        piece = Spaces[tpieced1]
        if Spaces[tpieced1] == piece and Spaces[tpieced2] == piece and Spaces[tpieced3] == piece and Spaces[tpieced4] == piece and piece != " ":
          declare_winner()
          return
      #Diagonal Down
      if col in "1234" and row in "def":
        if row == 'd':
          rowdes = 3
        elif row == 'e':
          rowdes = 4
        elif row == 'f':
          rowdes = 5
        tpieced1 = str(rows[rowdes]) + str(col)
        tpieced2 = str(rows[rowdes - 1]) + str(int(col) + 1)
        tpieced3 = str(rows[rowdes - 2]) + str(int(col) + 2)
        tpieced4 = str(rows[rowdes - 3]) + str(int(col) + 3)
        piece = Spaces[tpieced1]
        if Spaces[tpieced1] == piece and Spaces[tpieced2] == piece and Spaces[tpieced3] == piece and Spaces[tpieced4] == piece and piece != " ":
          declare_winner()
          return

def declare_winner():
  global Winner
  Winner = True

def get_col():
  return input("Column to drop " + CurrPlayer[1] + ": ")

Spaces = {"a1" : " ", "a2" : " ", "a3" : " ", "a4" : " ", "a5" : " ", "a6" : " ", "a7" : " ", "b1" : " ", "b2" : " ", "b3" : " ", "b4" : " ", "b5" : " ", "b6" : " ", "b7" : " ", "c1" : " ", "c2" : " ", "c3" : " ", "c4" : " ", "c5" : " ", "c6" : " ", "c7" : " ", "d1" : " ", "d2" : " ", "d3" : " ", "d4" : " ", "d5" : " ", "d6" : " ", "d7" : " ", "e1" : " ", "e2" : " ", "e3" : " ", "e4" : " ", "e5" : " ", "e6" : " ", "e7" : " ", "f1" : " ", "f2" : " ", "f3" : " ", "f4" : " ", "f5" : " ", "f6" : " ", "f7" : " "}
update_rows()

print("Hello, welcome to Connect 4!")
Player1 = [input("Please tell me who will be going first? This player will be Xs: "), "X"]
Player2 = [input("Now tell me who will be going second? This player will be Os: "), "O"]
input("Great! Let us begin. Press enter to start the game. ")
CurrPlayer = Player1
show_board()
Winner = False
while Winner == False:
  col = get_col()
  check_and_drop(col)
  CurrPlayer = switch_player(CurrPlayer)
  update_rows()
  check_winner()
  total_dropped += 1
  show_board()
  if total_dropped == 42:
    break
if Winner == True:
  print("Congragulations " + CurrPlayer[0] + ", you have won!")
elif total_dropped == 42:
  print("It looks like it's a tie! Thank you for playing.")