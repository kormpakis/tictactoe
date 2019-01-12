print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    game_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will play first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        print('Ok, see you another time!')
        break

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.            
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player1_marker, position)

            if win_check(game_board, player1_marker):
                display_board(game_board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.            
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player2_marker, position)

            if win_check(game_board, player2_marker):
                display_board(game_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
                    
    if not replay():
        print('Ok, see you another time!')
        break