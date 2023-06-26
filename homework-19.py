import random

board = [' '] * 9

PLAYER_X = 'X'
PLAYER_O = 'O'


def draw_board():
    print('---------')
    for i in range(0, 9, 3):
        print('|', board[i], '|', board[i + 1], '|', board[i + 2], '|')
        print('---------')


def check_win(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False


def make_move(player, position):
    if board[position] == ' ':
        board[position] = player
        return True
    else:
        return False


def computer_move():
    for i in range(9):
        if board[i] == ' ':
            board[i] = PLAYER_O
            if check_win(PLAYER_O):
                return i
            else:
                board[i] = ' '

    for i in range(9):
        if board[i] == ' ':
            board[i] = PLAYER_X
            if check_win(PLAYER_X):
                board[i] = PLAYER_O
                return i
            else:
                board[i] = ' '

    available_moves = [i for i in range(9) if board[i] == ' ']
    return random.choice(available_moves)


def play_game():
    current_player = random.choice([PLAYER_X, PLAYER_O])
    game_over = False

    while not game_over:
        draw_board()

        if current_player == PLAYER_X:
            print("Хід гравця X")
            while True:
                position = input("Введіть координату ходу (від 0 до 8): ")
                if not position.isdigit():
                    print("Неправильний хід. Введіть число від 0 до 8.")
                    continue
                position = int(position)
                if position < 0 or position > 8:
                    print("Неправильний хід. Введіть число від 0 до 8.")
                    continue
                if not make_move(PLAYER_X, position):
                    print("Неправильний хід. Спробуйте ще раз.")
                    continue
                break
        else:
            print("Хід комп'ютера O")
            position = computer_move()
            make_move(PLAYER_O, position)

        if check_win(current_player):
            draw_board()
            print("Гравець", current_player, "переміг!")
            game_over = True
        elif ' ' not in board:
            draw_board()
            print("Нічия!")
            game_over = True

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X


play_game()
