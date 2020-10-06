def init_board(size):
    # Funkcja tworzy tablicę o wymiarach ze zmiennej size
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
    if len(board) == 64:
        print("     1     2     3     4     5     6     7     8\n--------------------------------------------------")
        print(f"A |  {board[0]}  |  {board[1]}  |  {board[2]}  |  {board[3]}  |  {board[4]}  |  {board[5]}  |  {board[6]}  |  {board[7]}  \n--------------------------------------------------")
        print(f"B |  {board[8]}  |  {board[9]}  |  {board[10]}  |  {board[11]}  |  {board[12]}  |  {board[13]}  |  {board[14]}  |  {board[15]}\n--------------------------------------------------")
        print(f"C |  {board[16]}  |  {board[17]}  |  {board[18]}  |  {board[19]}  |  {board[20]}  |  {board[21]}  |  {board[22]}  |  {board[23]}\n--------------------------------------------------")
        print(f"D |  {board[24]}  |  {board[25]}  |  {board[26]}  |  {board[27]}  |  {board[28]}  |  {board[29]}  |  {board[30]}  |  {board[31]}  \n--------------------------------------------------")
        print(f"E |  {board[32]}  |  {board[33]}  |  {board[34]}  |  {board[35]}  |  {board[36]}  |  {board[37]}  |  {board[38]}  |  {board[39]}\n--------------------------------------------------")
        print(f"F |  {board[40]}  |  {board[41]}  |  {board[42]}  |  {board[43]}  |  {board[44]}  |  {board[45]}  |  {board[46]}  |  {board[47]}\n--------------------------------------------------")
        print(f"G |  {board[48]}  |  {board[49]}  |  {board[50]}  |  {board[51]}  |  {board[52]}  |  {board[53]}  |  {board[54]}  |  {board[55]}  \n--------------------------------------------------")
        print(f"H |  {board[56]}  |  {board[57]}  |  {board[57]}  |  {board[59]}  |  {board[60]}  |  {board[61]}  |  {board[62]}  |  {board[63]}\n--------------------------------------------------")
    if len(board) == 100:
        print("     1     2     3     4     5     6     7     8     9    10\n--------------------------------------------------------------")
        print(f"A |  {board[0]}  |  {board[1]}  |  {board[2]}  |  {board[3]}  |  {board[4]}  |  {board[5]}  |  {board[6]}  |  {board[7]}  |  {board[8]}  |  {board[9]}\n--------------------------------------------------------------")
        print(f"B |  {board[10]}  |  {board[11]}  |  {board[12]}  |  {board[13]}  |  {board[14]}  |  {board[15]}  |  {board[16]}  |  {board[17]}  |  {board[18]}  |  {board[19]}\n--------------------------------------------------------------")
        print(f"C |  {board[20]}  |  {board[21]}  |  {board[22]}  |  {board[23]}  |  {board[24]}  |  {board[25]}  |  {board[26]}  |  {board[27]}  |  {board[28]}  |  {board[29]}\n--------------------------------------------------------------")
        print(f"D |  {board[30]}  |  {board[31]}  |  {board[32]}  |  {board[33]}  |  {board[34]}  |  {board[35]}  |  {board[36]}  |  {board[37]}  |  {board[38]}  |  {board[39]}\n--------------------------------------------------------------")
        print(f"E |  {board[40]}  |  {board[41]}  |  {board[42]}  |  {board[43]}  |  {board[44]}  |  {board[45]}  |  {board[46]}  |  {board[47]}  |  {board[48]}  |  {board[49]}\n--------------------------------------------------------------")
        print(f"F |  {board[50]}  |  {board[51]}  |  {board[52]}  |  {board[53]}  |  {board[54]}  |  {board[55]}  |  {board[56]}  |  {board[57]}  |  {board[58]}  |  {board[59]}\n--------------------------------------------------------------")
        print(f"G |  {board[60]}  |  {board[61]}  |  {board[62]}  |  {board[63]}  |  {board[64]}  |  {board[65]}  |  {board[66]}  |  {board[67]}  |  {board[68]}  |  {board[69]}\n--------------------------------------------------------------")
        print(f"H |  {board[70]}  |  {board[71]}  |  {board[72]}  |  {board[73]}  |  {board[74]}  |  {board[75]}  |  {board[76]}  |  {board[77]}  |  {board[78]}  |  {board[79]}\n--------------------------------------------------------------")
        print(f"I |  {board[80]}  |  {board[81]}  |  {board[82]}  |  {board[83]}  |  {board[84]}  |  {board[85]}  |  {board[86]}  |  {board[87]}  |  {board[88]}  |  {board[89]}\n--------------------------------------------------------------")
        print(f"J |  {board[90]}  |  {board[91]}  |  {board[92]}  |  {board[93]}  |  {board[94]}  |  {board[95]}  |  {board[96]}  |  {board[97]}  |  {board[98]}  |  {board[99]}\n--------------------------------------------------------------")


    
    


def placement_phase(board, player):
    pass
    return board
    # Funkcja pozwala graczom na rozstawienie swoich statków


def get_move(board, player):
    pass
    return row, col
    return move = board[x]
    #Funkcja zwraca współrzędne ruchu lub miejsce w tablicy


def mark_shoot(board, shoot_board):
    pass
    # Funkcja odpowiedzialna za nadpisywanie odpowiedniej tablicy o ruchy graczy


def switch_player(player):
    pass
    # Funkcja zamienia turę player1 na player2


def check_win(player, board):
    pass
    return True / False
    # Funkcja do sprawdzania czy player wygrał


def battleship_game(mode, size):
    # Główna funkcja programu obsługująca poszczególne tury gry
    if mode == "H-H":
        pass
    if mode == "H-C":
        pass
    if mode == "C-H":
        pass


def size_choice():
    print("1.  5x5")
    print("2.  8x8")
    print("3.  10x10")
    size_choice = (input("Select size of game board: ")
    board_size = ""
    if size_choice == "1":
        board_size = 5
    if size_choice == "2":
        board_size = 8
    if size_choice == "3":
        board_size = 10
    else:
        print("Choose valid option!")
        size_choice()
    return board_size


def main_menu():
    # Funkcja programu pozwalająca na wybór trybu gry, inicjuje start gry
    print("GAME MODES:")
    print("1.HUMAN-HUMAN")
    print("2.HUMAN-COMPUTER")
    print("3.COMPUTER-HUMAN")
    select = input('Choose game mode: ')
    if select == str(1):
        game_mode = "H-H"
        size = size_choice()
        battleship_game(game_mode, size)
    elif select == str(2):
        game_mode = "H-C"
        size = size_choice()
        battleship_game(game_mode, size)
    elif select == str(3):
        game_mode = "C-H"
        size = size_choice()
        battleship_game(game_mode, size)     
    else:
        print("Choose valid option!")
        print_menu()


if __name__ == '__main__':
    main_menu()