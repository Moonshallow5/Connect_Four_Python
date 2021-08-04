class Model:
    the_board = {'7': ' ', '8': ' ', '9': ' ',
                 '4': ' ', '5': ' ', '6': ' ',
                 '1': ' ', '2': ' ', '3': ' '}
    yi = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ', ' ', ' ']]


player = 'X'

model = Model()


def is_move_valid(c):
    if c > 7 or c < 1:
        print("Enter value in range")
        return False
    if model.yi[0][c - 1] != ' ':
        return False

    else:
        return True


def board():
    for i in range(len(model.yi)):
        for j in range(len(model.yi[i])):
            print(model.yi[i][j], end=" ")
        print()


def is_wi_horizontal():
    for i in model.yi:
        rowCount = 0
        for j in i:
            if (j == player):
                rowCount += 1
            else:
                rowCount = 0
            if rowCount >= 3:
                return True


def is_win_vertical():
    for col in range(len(model.yi[0])):
        colCount=0
        for chars in model.yi:
            if(chars[col]==player):
                colCount+=1
            else:
                colCount=0
            if colCount>=3:
                return True


def yo(x):
    while not is_move_valid(x):
        x = int(input("Enter jnjn" + str(player) + ": "))
        is_move_valid(x)
    for row in range(len(model.yi) - 1, -1, -1):

        if model.yi[row][x - 1] == ' ':
            model.yi[row][x - 1] = player
            printsss()
            break


def labels():
    for i in range(7):
        print(end="  ")
        print('0' + str(i + 1), end="  ")


def win():
    i = 0
    printsss()
    while i == 0:
        x = int(input("Enter " + str(player) + ": "))
        yo(x)
        if (is_wi_horizontal()):
            break
        if(is_win_vertical()):
            break

        switch_players()


def printsss():
    rowDivider = "--------------------------------------------"
    print(rowDivider)
    for i in range(len(model.yi)):
        print("| ", end=" ")
        for j in range(len(model.yi[0])):
            print(model.yi[i][j], end=" ")
            print(" | ", end=" ")

        print()
        print(rowDivider)


def print_board(board):
    print('-------------')
    print('| ' + board['7'] + ' | ' + board['8'] + ' | ' + board['9'] + ' |')
    print('-------------')

    print()
    print('| ' + board['4'] + ' | ' + board['5'] + ' | ' + board['6'] + ' |')
    print('-------------')

    print()
    print('| ' + board['1'] + ' | ' + board['2'] + ' | ' + board['3'] + ' |')
    print('-------------')
    labels()
    print()


def switch_players():
    global player
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'


win()

printsss()
labels()
