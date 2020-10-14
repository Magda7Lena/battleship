
def init_board(size):
    number_of_fields =int(size) * int(size) 
    board = ['.' for x in range(number_of_fields)]
    return board

def print_board(board):
    if len(board) == 25:
        print("     1     2     3     4     5  \n---------------------------------")
        print(f"A |  {board[0]}  |  {board[1]}  |  {board[2]}  |  {board[3]}  |  {board[4]}  |\n---------------------------------")
        print(f"B |  {board[5]}  |  {board[6]}  |  {board[7]}  |  {board[8]}  |  {board[9]}  |\n---------------------------------")
        print(f"C |  {board[10]}  |  {board[11]}  |  {board[12]}  |  {board[13]}  |  {board[14]}  |\n---------------------------------")
        print(f"D |  {board[15]}  |  {board[16]}  |  {board[17]}  |  {board[18]}  |  {board[19]}  |\n---------------------------------")
        print(f"E |  {board[20]}  |  {board[21]}  |  {board[22]}  |  {board[23]}  |  {board[24]}  |\n---------------------------------")

def placement_phase(board, player):
    pass
    return board




print_board(placement_phase(init_board(5), 1))