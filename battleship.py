import os

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


def fillig_the_fields(field, board,):
    if len(board) == 25:
        comparative_list = ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "c1", "c2", "c3", "c4", "c5", "d1", "d2", "d3", "d4", "d5", "e1", "e2", "e3", "e4", "e5"]
        p = comparative_list.index(field)
        board[p] = "X"
        return board


def locate_filed(field, board):
     if len(board) == 25:
        comparative_list = ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "c1", "c2", "c3", "c4", "c5", "d1", "d2", "d3", "d4", "d5", "e1", "e2", "e3", "e4", "e5"]
        p = comparative_list.index(field)
        return p 



def placement_phase(board, player):
    if len(board) == 25:
        os.system('cls')
        print("=========================")
        print(f"Player {player} ordering phase")
        print("=========================")
        new_board = board
        print_board(new_board)
        print("Available ships: XX and XXX")
        print("Issue orders for first ship - XX")
        field_1 = input("Select first field that the ship will occupy: ")
        fillig_the_fields(field_1, new_board)
        field_2 = input("Select second field that the ship will occupy: ")
        fillig_the_fields(field_2, new_board)
        print_board(new_board)   
        print("Issue orders for second ship - XXX")
        field_1 = input("Select first field that the ship will occupy: ")
        fillig_the_fields(field_1, new_board)
        field_2 = input("Select second field that the ship will occupy: ")
        fillig_the_fields(field_2, new_board)
        field_3 = input("Select second field that the ship will occupy: ")
        fillig_the_fields(field_3, new_board)
        print_board(new_board) 
        return new_board


def check_shoot(board, index):
    if board[index] == "X":
        return True
    else:
        return False


def check_win(board):
    if "X" in board:
        return False
    if not "X" in board:
        return True


def get_valid_move(shooting_board):
    valid_moves = ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "c1", "c2", "c3", "c4", "c5", "d1", "d2", "d3", "d4", "d5", "e1", "e2", "e3", "e4", "e5"]
    move = input("Choose the field where you want your rockets to strike: ")

    if move in valid_moves:
        index = locate_filed(move, shooting_board)
        if shooting_board[index] == ".":
            return index
        if shooting_board[index] == "H" or shooting_board[index] == "M":
            print("You have already selected this field")
            get_valid_move(shooting_board)
    else:
        print("Invalid move")
        get_valid_move(shooting_board)


def battleship_game(mode, size):
    # Główna funkcja programu obsługująca poszczególne tury gry
    if mode == "H-H":
        players_board_1 = placement_phase(init_board(size), 1)
        shooting_board_1 = (init_board(size))
        my_board_1 = (init_board(size))
        players_board_2 = placement_phase(init_board(size), 2)
        shooting_board_2 = (init_board(size))
        my_board_2 = (init_board(size))
        os.system('cls')
        player = 1
        while check_win(players_board_1) == False and check_win(players_board_2) == False:
            if player == 1:
                print("=========================")
                print(f"Player {player} ")
                print("=========================")
                print_board(shooting_board_1)
                index = get_valid_move(shooting_board_1)
                os.system('cls')
                flag = check_shoot(players_board_2, index)
                if flag == True:
                    print("=========================")
                    print(f"Player {player} ")
                    print("=========================")
                    print("You've hit a ship!")
                    print("=========================")
                    shooting_board_1[index] = "H"
                    my_board_2[index] = "H"
                    players_board_2[index] = "H"
                if flag == False:
                    print("=========================")
                    print(f"Player {player} ")
                    print("=========================")
                    print("You've missed!")
                    print("=========================")
                    shooting_board_1[index] = "M"
                    my_board_2[index] = "M"
                print("Enemy map - Your moves")
                print("H - hit")
                print("M - missed")
                print("=========================")
                print_board(shooting_board_1)
                print("=========================")
                print(" ")
                print("=========================")
                print("Your map - Enemy moves")
                print("H - hit")
                print("M - missed")
                print("=========================")
                print_board(my_board_1)
                if check_win(players_board_2) == True:
                    print("=========================")
                    print("Player 1 WON!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("=========================")
                    main_menu()
                x = input(" ")
                os.system('cls')
                player = 2
            if player == 2:
                print("=========================")
                print(f"Player {player} ")
                print("=========================")
                print_board(shooting_board_2)
                index = get_valid_move(shooting_board_2)
                os.system('cls')
                flag = check_shoot(players_board_1, index)
                if flag == True:
                    print("=========================")
                    print(f"Player {player} ")
                    print("=========================")
                    print("=========================")
                    print("You've hit a ship!")
                    print("=========================")
                    shooting_board_2[index] = "H"
                    my_board_1[index] = "H"
                    players_board_1[index] = "H"
                if flag == False:
                    print("=========================")
                    print(f"Player {player} ")
                    print("=========================")
                    print("You've missed!")
                    print("=========================")
                    shooting_board_2[index] = "M"
                    my_board_1[index] = "M"
                print("Enemy map - Your moves")
                print("H - hit")
                print("M - missed")
                print("=========================")
                print_board(shooting_board_2)
                print("=========================")
                print(" ")
                print("=========================")
                print("Your map - Enemy moves")
                print("H - hit")
                print("M - missed")
                print("=========================")
                print_board(my_board_2)
                if check_win(players_board_1) == True:
                    print("=========================")
                    print("Player 2 WON!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print("=========================")
                    main_menu()
                x = input(" ")
                os.system('cls')
                player = 1
    if mode == "H-C":
        pass
    if mode == "C-H":
        pass


def size_choice():
    print("Sizes: ")
    print("1.  5x5")
    print("2.  8x8")
    print("3.  10x10")
    size_choice = (input("Select size of game board: "))
    board_size = 0
    if size_choice == "1":
        board_size = 5
        return board_size
    if size_choice == "2":
        board_size = 8
        return board_size
    if size_choice == "3":
        board_size = 10
        return board_size
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
        os.system('cls')
        size = size_choice()
        os.system('cls')
        battleship_game(game_mode, size)
    elif select == str(2):
        pass
        game_mode = "H-C"
        size = size_choice()
        battleship_game(game_mode, size)
    elif select == str(3):
        pass
        game_mode = "C-H"
        size = size_choice()
        battleship_game(game_mode, size)     
    else:
        print("Choose valid option!")
        print_menu()


if __name__ == '__main__':
    main_menu()
