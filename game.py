from tabulate import tabulate
import random


class TicTacToe:

    def __init__(self):
        self.board_data = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.board_head = ['TIC', 'TAC', 'TOE']
        horizontal = ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']
        diagonal = ['1', '5', '9'], ['3', '5', '9']
        vertical = ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']
        self.computer_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.winning_scenarios = [horizontal, diagonal, vertical]
        self.game_board = tabulate(self.board_data, headers=self.board_head, tablefmt="grid")
        self.player1score = 0
        self.player2score = 0
        self.computerscore = 0
        self.game = True

    def game_board(self):
        game_board = tabulate(self.board_data, headers=self.board_head, tablefmt="grid")

    def reset_board(self):
        self.board_data = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.board_head = ['TIC', 'TAC', 'TOE']
        horizontal = ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']
        diagonal = ['1', '5', '9'], ['3', '5', '9']
        vertical = ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']
        self.computer_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.winning_scenarios = [horizontal, diagonal, vertical]
        self.game_board = tabulate(self.board_data, headers=self.board_head, tablefmt="grid")
        self.game = True

    def reset_game(self, player1, player2):
        continue_game = input('do you want to play again? Yes or No? ').lower()
        if continue_game == 'yes':
            player1score = self.player1score
            computerscore = self.computerscore
            player2score = self.player2score
            self.game = True
            self.reset_board()
            turn = 1
            if player2 == None:
                print(
                    f'{player1.upper()} SCORE: {player1score}      COMPUTER SCORE: {computerscore}\nTurn: {turn}\n{self.game_board}')
                new_result = self.check_who_is_first(player1=player1, player2=None, winner=self.winner)
                self.single_player_mode(result=new_result, player1=player1, turn=turn)
            else:
                print(
                    f'{player1.upper()} SCORE: {player1score}      {player2.upper()} SCORE: {player2score}\nTurn: {turn}\n{self.game_board}')
                new_result = self.check_who_is_first(player1=player1, player2=player2, winner=self.winner)
                self.multiplayer_mode(result=new_result, player1=player1, player2=player2, turn=turn)

    def check_who_is_first(self,player1,player2,winner):
        if player2 == None:
            list_of_players = [player1,'computer']
            random_pick_who_goes_first_list = random.choice(list_of_players)
            list_for_player_who_is_not_first = [item for item in list_of_players if item != random_pick_who_goes_first_list]

            if winner == None:

                player_order_dictionary = {'First':random_pick_who_goes_first_list,'Second':list_for_player_who_is_not_first[0]}
            else:
                player_order_dictionary = {'First':winner,'Second':list_for_player_who_is_not_first[0]}

            return player_order_dictionary
        else:
            list_of_players = [player1, player2]
            random_pick_who_goes_first_list = random.choice(list_of_players)
            list_for_player_who_is_not_first = [item for item in list_of_players if
                                                item != random_pick_who_goes_first_list]
            if winner == None:
                player_order_dictionary = {'First': random_pick_who_goes_first_list,
                                       'Second': list_for_player_who_is_not_first[0]}
            else:
                player_order_dictionary = {'First':winner,'Second':list_for_player_who_is_not_first[0]}

            return player_order_dictionary

    def x_or_o(self,choice,turn):
        for data in self.board_data:
            if choice in data:
                for position in self.winning_scenarios:
                    for answer in position:
                        if choice in answer:
                            answer_index = answer.index(choice)
                            if turn % 2 == 0:
                                answer[answer_index] = 'o'
                            else:
                                answer[answer_index] = 'x'
                        if turn % 2 == 0:
                            newdata = ['o' if item == choice else item for item in answer]
                        else:
                            newdata = ['x' if item == choice else item for item in answer]
                        answer = newdata
                self.computer_choices.remove(choice)
                data_list_index = self.board_data.index(data)
                if turn % 2 == 0:
                    newdata = ['o' if item == choice else item for item in data]
                else:
                    newdata = ['x' if item == choice else item for item in data]
                self.board_data[data_list_index] = newdata

                self.game_board = tabulate(self.board_data, headers=self.board_head, tablefmt='grid')

    def computer(self, turn):
        computer_choice = random.choice(self.computer_choices)
        self.x_or_o(computer_choice, turn)

    def player(self,choice,turn):
        self.x_or_o(choice,turn)

    def check_for_winner_loser_tie(self, turn, result, player1, player2):
        for position in self.winning_scenarios:
            for something in position:
                if something == ['x', 'x', 'x']:
                    print(f"{result['First']} is the winner!")
                    self.winner = result['First']
                    if player2 == None:
                        if result['First'] == player1:
                            self.player1score += 1
                        else:
                            self.computerscore += 1
                    else:
                        if result['First'] == player1:
                            self.player1score += 1
                        else:
                            self.player2score += 1
                    self.game = False
                else:
                    if something == ['o', 'o', 'o']:
                        print(f"{result['Second']} is the winner!")
                        self.winner = result['Second']
                        if player2 == None:
                            if result['Second'] == player1:
                                self.player1score += 1
                            else:
                                self.computerscore += 1
                        else:
                            if result['Second'] == player1:
                                self.player1score += 1
                            else:
                                self.player2score += 1
                        self.game = False
            if turn >= 10 and self.game == True:
                print('tie')
                self.winner = None
                self.game = False

    def single_player_mode(self, result, player1, turn):
        while self.game:
            if result['First'] == player1:
                if turn % 2 == 0:
                    self.computer(turn)
                else:
                    choice = input('choose a position ')
                    self.player(choice, turn)
            else:
                if turn % 2 == 0:
                    choice = input('choose a position ')
                    self.player(choice, turn)
                else:
                    self.computer(turn)
            turn += 1
            print(f'{player1.upper()} SCORE: {self.player1score}      COMPUTER SCORE: {self.computerscore}\nTurn: {turn}\n{self.game_board}')
            self.check_for_winner_loser_tie(turn, result=result, player1=player1, player2=None)

    def multiplayer_mode(self, result, player1, player2, turn):
        while self.game:
            if result['First'] == player1:
                if turn % 2 == 0:
                    player_2_choice = input('choose a position ')
                    self.player(player_2_choice, turn)
                else:
                    choice = input('choose a position ')
                    self.player(choice, turn)
            else:
                if turn % 2 == 0:
                    choice = input('choose a position ')
                    self.player(choice, turn)
                else:
                    player_2_choice = input('choose a position ')
                    self.player(player_2_choice, turn)
            turn += 1
            print(f'{player1.upper()} SCORE: {self.player1score}      {player2.upper()} SCORE: {self.player2score}\nTurn: {turn}\n{self.game_board}')
            self.check_for_winner_loser_tie(turn, result=result, player1=player1, player2=True)










