import os
import random


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_board(board):
    cls()  # clear screen
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def player_input():
    marker = ''
    while not(marker == 'X' or marker == 'O'):
        marker = input('Player 1, choose X or O: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return((board[1] == board[2] == board[3] == mark) or
           (board[4] == board[5] == board[6] == mark) or
           (board[7] == board[8] == board[9] == mark) or
           (board[1] == board[4] == board[7] == mark) or
           (board[2] == board[5] == board[8] == mark) or
           (board[3] == board[6] == board[9] == mark) or
           (board[1] == board[5] == board[9] == mark) or
           (board[3] == board[5] == board[7] == mark))


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board, player):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input(player + ', Choose a position (1-9): '))
    return position


def replay():
    choice = ''
    while not(choice == 'Y' or choice == 'N'):
        choice = input('Play again? Enter Y or N: ').upper()
    return choice == 'Y'


def tictactoe():
    print('Welcome')
    while True:
        game_board = ['#'] + [' '] * 9
        player1_marker, player2_marker = player_input()

        turn = choose_first()
        print(turn + ' goes first')

        play_game = ''
        while not(play_game == 'Y' or play_game == 'N'):
            play_game = input('Ready to play? Y or N? ').upper()
        if play_game == 'Y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                display_board(game_board)
                position = player_choice(game_board, turn)
                place_marker(game_board, player1_marker, position)

                if win_check(game_board, player1_marker):
                    display_board(game_board)
                    print('Player 1 has won!')
                    game_on = False
                else:
                    if full_board_check(game_board):
                        display_board(game_board)
                        print('Game Tied!')
                        game_on = False
                    else:
                        turn = 'Player 2'

            else:
                display_board(game_board)
                position = player_choice(game_board, turn)
                place_marker(game_board, player2_marker, position)

                if win_check(game_board, player2_marker):
                    display_board(game_board)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(game_board):
                        display_board(game_board)
                        print('Game Tied!')
                        game_on = False
                    else:
                        turn = 'Player 1'

        if not replay():
            break


if __name__ == '__main__':
    tictactoe()
