from game import TicTacToe

tictactoe = TicTacToe()
game = True
turn = 1
player_mode = input("Press '1' to test your skills against the computer.\nPress '2' to play against a friend! ")

if player_mode == '1':
    player1 = input('who is playing: ')
    player1score = tictactoe.player1score
    computerscore = tictactoe.computerscore
    print(f'{player1.upper()} SCORE: {player1score}      COMPUTER SCORE: {computerscore}\nTurn: {turn}\n{tictactoe.game_board}')
    result = tictactoe.check_who_is_first(player1=player1,player2=None,winner=None)
    tictactoe.single_player_mode(result,player1,turn)
    while tictactoe.game != True:
        tictactoe.reset_game(player1,player2=None)

else:
    player1 = input('who is playing: ')
    player2 = input('who is playing: ')
    player1score = tictactoe.player1score
    player2score = tictactoe.player2score
    print(f'{player1.upper()} SCORE: {player1score}      {player2.upper()} SCORE: {player2score}\nTurn: {turn}\n{tictactoe.game_board}')
    result = tictactoe.check_who_is_first(player1=player1,player2=player2,winner=None)
    tictactoe.multiplayer_mode(result,player1,player2,turn)
    while tictactoe.game != True:
        tictactoe.reset_game(player1=player1,player2=player2)
