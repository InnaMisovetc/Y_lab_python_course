from task2.app.game_board import GameBoard


def restart_game_dialogue():
    """ Asks user whether he wants to restart the game. Returns True if the user enters yes.
    Returns False if the user enters no. Otherwise, asks again to choose yes or no. """

    choice = input('Do you want to play again? Enter yes or no: ').strip().upper()
    if choice == 'YES':
        return True
    elif choice == 'NO':
        return False
    else:
        print('Enter YES or NO')
        return restart_game_dialogue()


def main():
    while True:
        new_board = GameBoard()
        new_board.start_game()
        print(new_board.draw_board())
        while True:
            row, column = new_board.current_player.select_cell(new_board)
            if not new_board.play_round(row, column):
                break
        if not restart_game_dialogue():
            break


if __name__ == '__main__':
    main()
