class Model:
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


def initial():
    for i in range(len(model.yi)):
        for j in range(len(model.yi[i])):
            model.yi[i][j] = ' '


def is_wi_horizontal():
    for i in model.yi:
        rowCount = 0
        for j in i:
            if j == player:
                rowCount += 1
            else:
                rowCount = 0
            if rowCount >= 3:
                return True


def is_win_vertical():
    for col in range(len(model.yi[0])):
        colCount = 0
        for chars in model.yi:
            if chars[col] == player:
                colCount += 1
            else:
                colCount = 0
            if colCount >= 3:
                return True


def yo(x):
    while not is_move_valid(x):
        x = int(input("Enter " + str(player) + ": "))
        is_move_valid(x)
    for row in range(len(model.yi) - 1, -1, -1):

        if model.yi[row][x - 1] == ' ':
            model.yi[row][x - 1] = player
            prints()
            labels()
            if model.yi[0][x - 1] == player:
                available.remove(x)
            print()
            break


def labels():
    for i in range(7):
        print(end="  ")
        print('0' + str(i + 1), end="  ")


winX = 0
winY = 0
available = [1, 2, 3, 4, 5, 6, 7]


def win():
    global winX
    global winY
    i = 0
    prints()
    labels()
    print()
    global available
    available = [1, 2, 3, 4, 5, 6, 7]
    while i == 0:
        print("Available numbers are: " + str(available))
        x = int(input("Enter " + str(player) + ": "))
        yo(x)
        if is_wi_horizontal():
            print(str(player) + " won by horizontal win")
            if player == 'X':
                winX += 1
            elif player == 'Y':
                winY += 1
            break
        elif is_win_vertical():
            print(str(player) + " won by vertical win")
            if player == 'X':
                winX += 1
            elif player == 'Y':
                winY += 1
            break

        switch_players()
    print("Score is " + str(winX) + " to X and " + str(winY) + " to Y")
    play_again()


def play_again():
    print("Would you like to play again? Enter Y to play again and N to stop playing")
    x = input()
    if x == 'Y':
        initial()
        win()
    else:
        print("Good game")


def prints():
    rowDivider = "--------------------------------------------"
    print(rowDivider)
    for i in range(len(model.yi)):
        print("| ", end=" ")
        for j in range(len(model.yi[0])):
            print(model.yi[i][j], end=" ")
            print(" | ", end=" ")

        print()
        print(rowDivider)


def switch_players():
    global player
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'


win()
