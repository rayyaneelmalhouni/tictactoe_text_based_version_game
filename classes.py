
class Game:

    def __init__(self):
        self.game_is_on = None
        self.turn_is_on = True
        self.turn_num = 1
        self.cells = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.player_turn = 0

    def display_board(self):
        """Display the tic-tac-toe board"""
        display = ""
        for i in range(3):
            display += f" {self.cells[i*3]} | {self.cells[i*3 + 1]} | {self.cells[i*3 + 2]}\n"
            if not i == 2:
                display += "___________\n"
        return display

    def switch_player_turn(self):
        """Switch players turn"""
        if self.player_turn == 0:
            self.player_turn = 1
        else:
            self.player_turn = 0

    def check_win(self):
        """Check if the player has won"""
        for i in range(3):
            if (self.cells[i*3] == self.cells[i*3 + 1] == self.cells[i*3 + 2]) \
                    or (self.cells[i] == self.cells[i + 3] == self.cells[i + 6]):
                self.turn_is_on = False
                return True
        if self.cells[0] == self.cells[4] == self.cells[8] or self.cells[2] == self.cells[4] == self.cells[6]:
            self.turn_is_on = False
            return True
        return False

    def check_draw(self):
        """Check if there is a draw"""
        for cell in self.cells:
            if cell not in "XO":
                return False
        self.turn_is_on = False
        return True

    def replay(self):
        """Ask players if they want to play in another turn"""
        decision = input("Do you want to move to the next turn? (yes/no): ").lower()
        if decision == "yes":
            self.turn_num += 1
            self.turn_is_on = True
            self.cells = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            return True
        else:
            self.game_is_on = False
            return False

    def ask_to_play(self):
        """Ask players if they want to play"""
        decision = input("Do you want to play? (yes/no): ").lower()
        if decision == "yes":
            self.game_is_on = True
            return True
        else:
            self.game_is_on = False
            return False

    def print_scores(self, player_a, player_b):
        """Print the current Players scores with their names"""
        return f"Player {player_a.name} score is: {player_a.score}\n" \
               f"Player {player_b.name} score is: {player_b.score}"


class Player:

    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
        self.score = 0

    def choose(self, game: Game):
        """Let the player choose a cell and put on it his symbol"""
        has_chose = False
        while not has_chose:
            cell = input(f"Player {self.name} to Play: ")
            if cell not in "XO":
                if cell in game.cells:
                    cell_index = game.cells.index(cell)
                    game.cells[cell_index] = self.symbol
                    has_chose = True
                else:
                    print("Please enter the corresponding cell number")
            else:
                print("You can't over right the content of a cell, Please try again")

    def won(self):
        print(f"Player {self.name} has won!")
        self.score += 1


