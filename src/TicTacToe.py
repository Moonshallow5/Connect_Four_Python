def print_board(board):
    print('-------------')
    print('| ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'] + ' |')
    print('-------------')
    labels3()
    print()
    print('| ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'] + ' |')
    print('-------------')

    labels2()
    print()
    print('| ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'] + ' |')
    print('-------------')

    labels()
    print()


def is_move_valid(x):
    if x > 9 or x <= 0:
        print("Please enter value in range")
        return False
    elif model.the_board['{}'.format(x)] == 'X' or model.the_board['{}'.format(x)] == 'O':
        print("Board is full")
        return False
    else:
        return True


class Model:
    the_board = {'7': ' ', '8': ' ', '9': ' ',
                 '4': ' ', '5': ' ', '6': ' ',
                 '1': ' ', '2': ' ', '3': ' '}


model = Model()


def labels3():
    for i in range(6, 9, 1):
        print(end="  ")
        print(str(i + 1), end=" ")


def labels():
    for i in range(3):
        print(end="  ")
        print(str(i + 1), end=" ")


def labels2():
    for i in range(3, 6, 1):
        print(end="  ")
        print(str(i + 1), end=" ")


player = 'X'


def switch_players():
    global player

    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'


def is_winner_upward_diagonal():
    if model.the_board['1'] == player and model.the_board['5'] == player and model.the_board['9'] == player:
        return True


def is_winner_vertical():
    count = 0
    ss1 = 0
    kl = 1
    while ss1 <= 2:
        for i in range(kl, 10, 3):
            if model.the_board['{}'.format(i)] == player:
                count += 1
                if count >= 3:
                    return True
        ss1 += 1
        count = 0
        kl += 1


def is_winner_horizontal():
    count = 0
    ss1 = 0
    kl = 1
    while ss1 <= 2:
        for i in range(kl, kl + 3, 1):

            if model.the_board['{}'.format(i)] == player:
                count += 1

                if count >= 3:
                    return True
        ss1 += 1
        count = 0
        kl += 3


def is_winner_downward_diagonal():
    if model.the_board['7'] == player and model.the_board['5'] == player and model.the_board['3'] == player:
        return True


wonX = 0
wonO = 0


def concede(x):
    global wonX, wonO
    if x == -1:
        switch_players()
        print(str(player) + " wins")
        if player == 'X':
            wonX += 1
        elif player == 'O':
            wonO += 1
        print("Score is " + str(wonX) + " to X and " + str(wonO) + " to O")
        return True


def some():
    global wonX
    global wonO
    print(str(player) + " wins")
    if is_winner_upward_diagonal():
        print("Due to upward diagonal win")
    elif is_winner_horizontal():
        print("Due to horizontal win")
    elif is_winner_vertical():
        print("Due to vertical win")
    elif is_winner_downward_diagonal():
        print("Due to downward diagonal win")

    if player == 'X':
        wonX += 1

    elif player == 'O':
        wonO += 1
    print("Score is " + str(wonX) + " to X and " + str(wonO) + " to O")


def play_again():
    print("Would you like to play again Enter Y to play again")
    y = input("Enter: ")
    if y == "Y":
        model.the_board['1'] = ' '
        model.the_board['2'] = ' '
        model.the_board['3'] = ' '
        model.the_board['4'] = ' '
        model.the_board['5'] = ' '
        model.the_board['6'] = ' '
        model.the_board['7'] = ' '
        model.the_board['8'] = ' '
        model.the_board['9'] = ' '
        print_board(model.the_board)
        if player == 'O':
            switch_players()
        game()


ss = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def win():
    count = 0
    i = 0
    global ss
    ss = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while i == 0:
        print("Available moves: " + str(ss))
        x = int(input("Enter" + str(player) + ": "))
        if x != -1:
            yo(x)
            count += 1
            print_board(model.the_board)

            print()
            if is_winner_vertical():
                some()
                break
            elif is_winner_horizontal():
                some()
                break
            elif is_winner_upward_diagonal():
                some()
                break
            elif is_winner_downward_diagonal():
                some()
                break
            if count == 9:
                print("Tie Game")
                break

            switch_players()
        else:
            concede(x)
            break


def yo(x):
    while not is_move_valid(x):
        print("Try again")
        x = int(input("Enter " + str(player) + ": "))
        is_move_valid(x)
    ss.remove(x)
    model.the_board['{}'.format(x)] = player


def game():
    win()
    play_again()


print("Enter -1 to concede")
print_board(model.the_board)
game()
