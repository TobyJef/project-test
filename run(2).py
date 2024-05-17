import random
import time

title = ("\n", "  ", "*" * 3, "Starfighters", "*" * 3, "\n")


# Opening message to the player
print("\n", "  ", "*" * 3, "Welcome to Starfighters", "*" * 3, "\n")

# Player name entry
username = input("Please enter your name: \n")
print("\n")
print("Welcome, Admiral", username, "\n")
print("Admiral", username, ",your fleet is in position and awaiting your command.", "\n" * 2,)

# Gameboard key
print("Key:", "\n", "H = Hit", "\n", "o = Miss", "\n", "* = Starfighter", "\n")


class GameBoard:
    """
    Creates game boards
    """
    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers():
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F":5, "G":6, "H":7}
        return letters_to_numbers

    def print_board(self):
        """
        Prints players game boards
        """
        print("  A B C D E F G H")
        print("  ---------------")
        row_number = 1
        for row in board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1 


class Battleship:
    def __init__(self,board):
        self.board = board
    
    def create_ships(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def get_user_input(self):
        try:
            x_row = input("Enter the row of the ship: ")
            while x_row not in '12345678':
                print('Please choose a row between 1-8')
                x_row = input("Enter the row of the ship: ")

            y_column = input("Enter the column letter of the ship: ").upper()
            while y_columnnot in "ABCDEFGH":
                print("Please enter a column between A-H")
                y_column = input("Enter the column letter of the ship: ").upper()
            return int(x_row) - 1, GameBoard.get_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input")
            return self.get_user_input()

    
def count_hit_ships(self):
    hit_ships = 0
    for row in self.board:
        for column in row:
            if column -- "X":
                hit_ships += 1
    return hit_ships


def RunGame():
    computer_board = Gameboard([[" "] * 8 for i in range(8)])
    user_guess_board = GameBoard([[" "] * 8 for i in range(8)])
    Battleship.create_ships(computer_board)
    #start 10 turns
    turns = 10
    while turns > 0:
        GameBoard.print_board(user_guess_board)
        #get user input
        user_x_row, user_y_column = Battleship.get_user_input(object)
        #check if duplicate guess
        while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_goard
        board[user_x_row][user_y_column] == "X":
        print("You guess that co-oridinate already")
        user_x_row, user_y_column = Battleship.get_user_input(object)

