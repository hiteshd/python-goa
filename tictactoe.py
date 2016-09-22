import random
import sys

game_grid = """
 %s | %s | %s
---+---+---
 %s | %s | %s
---+---+---
 %s | %s | %s
"""

WINNING_POSITIONS = [{1,2,3}, {4,5,6}, {7,8,9}, {1,5,9}, {1,4,7}, {2,5,8}, {3,6,9}, {3,5,7}]

COMPUTER = 'O'
PLAYER = 'X'

class TicTacToe(object):

    def __init__(self):
        self.all_played = set([])
        self.user_played = set([])
        self.computer_played = set([])
        self.board_status = {}

    def show_board(self):
        return game_grid % (
            self.board_status.get(1, '1'),
            self.board_status.get(2, '2'),
            self.board_status.get(3, '3'),
            self.board_status.get(4, '4'),
            self.board_status.get(5, '5'),
            self.board_status.get(6, '6'),
            self.board_status.get(7, '7'),
            self.board_status.get(8, '8'),
            self.board_status.get(9, '9')
        )

    def _random_play(self):
        return random.choice(list(set(range(1,10)) - self.all_played))

    def is_all_played(self):
        if len(self.all_played) == 9:
            return True
        else:
            return False

    def play_at_position(self, position, mark):
        mark = mark.upper()
        if mark == 'X' or mark == 'O':
            if mark == 'X':
                self.user_played.add(position)
            else:
                self.computer_played.add(position)
            self.all_played.add(position)
            if self.board_status.get(position, False):
                print "Position is already occupied"
            else:
                self.board_status[position] = mark
        else:
            print "You need to enter X or O"

    def computer_play(self):
        position = self._random_play()
        print "The computer played at position:", position
        self.play_at_position(position, COMPUTER)

    def check_win(self):
        """
        First check if user won
        """
        for win_position in WINNING_POSITIONS:
            if win_position.issubset(self.user_played):
                print "User Won!"
                return True
            if win_position.issubset(self.computer_played):
                print "Computer Won!"
                return True

        return False

print "Welcome to Tic Tac Toe. "
print "Your marker on the board is:", PLAYER
print "Enter the position from 1 to 9 on the board below to play"
print "You get the starting chance\n"
ttt_object = TicTacToe()

while True:
    if not ttt_object.check_win():
        if not ttt_object.is_all_played():
            print ttt_object.show_board()
            try:
                user_input = int(raw_input("Enter Position to play: "))
            except KeyboardInterrupt:
                print "You pressed Ctrl+c"
                break
            except:
                print "Your input is invalid. give me a number from 1 to 9"
                continue
            if user_input > 9 or user_input < 1:
                print "Position should be between 1 and 9. You lose a chance"
            else:
                ttt_object.play_at_position(user_input, PLAYER)
            if not ttt_object.is_all_played():
                ttt_object.computer_play()
        else:
            print "Its a draw"
            break
    else:
        break
