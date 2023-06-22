# Imports
from classes import Game, Player

# Salutation
print("Welcome to the Text Based Tic Tac Toe Game")

# Creating the game and players
game = Game()
player1 = Player(symbol="X", name="1")
player2 = Player(symbol="O", name="2")
players = [player1, player2]

game.ask_to_play()
while game.game_is_on:
    print(game.print_scores(player1, player2))
    print(f"Turn number: {game.turn_num}")
    print(game.display_board())
    while game.turn_is_on:
        player = players[game.player_turn]
        player.choose(game)
        print(game.display_board())
        if game.check_win():
            player.won()
        elif game.check_draw():
            print("You draw")
        game.switch_player_turn()
    if not game.replay():
        print(game.print_scores(player1, player2))

