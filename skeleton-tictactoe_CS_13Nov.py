

def create_zero_matrix(r, c):
    output = []
    for _ in range(r):
        row = []
        for _ in range(c):
            row.append(0)
        output.append(row)
    return output


def print_ttt(game):
    for i in range(3):
        print(f'{game[i][0]}|{game[i][1]}|{game[i][2]}')
        if i != 2:
            print('-----')


piece = ['X', 'O']


def check_valid_move(game, inp):
    if inp > 9 or inp < 1:
        return False
    i = (inp-1)//3
    j = (inp-1)%3
    if game[i][j] == 'X' or game[i][j] =='O':
        return False
    return True


def check_win(game):
    for i in range(3):
        if game[i][0] == game[i][1] and game[i][1] == game[i][2]:
            if game[i][0] == piece[0] or game[i][0]== piece[1]:
                return game[i][0]
    for j in range(3):
        if game[0][j] == game[1][j] and game[1][j] == game[2][j]:
            if game[0][j] == piece[0] or game[0][j]== piece[1]:
                return game[0][j]
    if game[0][2] == game[1][1] and game[1][1] == game[2][0]:
        if game[0][2] == piece[0] or game [0][2] == piece[1]:
            return game[0][2]
    if game[0][0] == game[1][1] and game[1][1] == game[2][2]:
        if game[0][0] == piece[0] or game[0][0] == piece[1]:
            return game[0][0]
    return False


def ttt_gameplay():
    game = create_zero_matrix(3, 3)
    for i in range(3):
        for j in range(3):
            game[i][j] = i*3+j+1
            
    player = 0
    Turn = 0
    print_ttt(game)
    print()
    while True:
        if Turn == 9:
            print("It is a tie!")
            break

        pos = int(input(f'Player {piece[player]} move:')) 
        valid_move = check_valid_move(game,pos)
        if valid_move:
            i = (pos-1)//3
            j = (pos-1)%3
            game[i][j] = piece[player]
            Turn += 1
            print_ttt(game)
            winner_found = check_win(game)
            if winner_found:
                print(f"Player {winner_found} won!")
                break
            player = 1 - player
            print()
        else:
            print(f"Invalid move!")
            

