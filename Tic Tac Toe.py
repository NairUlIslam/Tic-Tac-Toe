import sys

player = True

board = [''] * 10


def display_board(board):
    print("\n")
    print(board[7] + '     |  ' + board[8] + '     |  ' + board[9])
    print("____________________")
    print(board[4] + '     |  ' + board[5] + '     |  ' + board[6])
    print("____________________")
    print(board[1] + '     |  ' + board[2] + '     |  ' + board[3])


while True:

    display_board(board)


    def chk_status():

        if ((board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or
                (board[4] == 'X' and board[5] == 'X' and board[6] == 'X') or
                (board[7] == 'X' and board[8] == 'X' and board[9] == 'X') or
                (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or
                (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or
                (board[3] == 'X' and board[6] == 'X' and board[9] == 'X') or
                (board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or
                (board[3] == 'X' and board[5] == 'X' and board[7] == 'X')):
            print("Game won by player 1")
            print("exiting")
            sys.exit(0)

        if ((board[1] == '0' and board[2] == '0' and board[3] == '0') or
                (board[4] == '0' and board[5] == '0' and board[6] == '0') or
                (board[7] == '0' and board[8] == '0' and board[9] == '0') or
                (board[1] == '0' and board[4] == '0' and board[7] == '0') or
                (board[2] == '0' and board[5] == '0' and board[8] == '0') or
                (board[3] == '0' and board[6] == '0' and board[9] == '0') or
                (board[1] == '0' and board[5] == '0' and board[9] == '0') or
                (board[3] == '0' and board[5] == '0' and board[7] == '0')):
            print("Game won by player 2")
            print("exiting")
            sys.exit(0)

        elif ((board[1] == 'X' or board[1] == '0') and (board[2] == 'X' or board[2] == '0')
              and (board[3] == 'X' or board[3] == '0') and

              (board[4] == 'X' or board[4] == '0') and (board[5] == 'X' or board[5] == '0')
              and (board[6] == 'X' or board[6] == '0') and

              (board[7] == 'X' or board[7] == '0') and (board[8] == 'X' or board[8] == '0')
              and (board[9] == 'X' or board[9] == '0') and

              (board[1] == 'X' or board[1] == '0') and (board[4] == 'X' or board[4] == '0')
              and (board[7] == 'X' or board[7] == '0') and

              (board[2] == 'X' or board[2] == '0') and (board[5] == 'X' or board[5] == '0')
              and (board[8] == 'X' or board[8] == '0') and

              (board[3] == 'X' or board[3] == '0') and (board[6] == 'X' or board[6] == '0')
              and (board[9] == 'X' or board[9] == '0') and

              (board[1] == 'X' or board[1] == '0') and (board[5] == 'X' or board[5] == '0')
              and (board[9] == 'X' or board[9] == '0') and

              (board[3] == 'X' or board[3] == '0') and (board[5] == 'X' or board[5] == '0')
              and (board[7] == 'X' or board[7] == '0')):

            print("It is a Tie.")
            print("Exiting")
            sys.exit(0)


    def chk_player():
        global player
        if player is True:
            print("Player 1's turn")
            return True
        elif player is False:
            print("player 2's turn")
            return False


    def make_move():
        global board
        global player
        global pos
        if chk_player():
            print("enter the value for an unmarked position by using the numpad")
            try:
                pos = int(input())
            except ValueError:
                print("Press valid numpad buttons [1-9], Try again")
                make_move()
            board[pos] = 'X'
            player = False
        else:
            print("enter the value for an unmarked position by using the numpad")
            try:
                pos = int(input())
            except ValueError:
                print("Press valid numpad buttons [1-9], Try again")
                make_move()
            board[pos] = '0'
            player = True


    make_move()

    chk_status()
