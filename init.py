from game_of_life import Game_of_life
game = Game_of_life()

size = int(input('Quelle taille de grille voulez-vous ?\n'))
pop = float(input('Quelle part de population initiale (<1)?\n'))
game.__init__(size)
iterations = int(input('Combien d\'itérations voulez-vous ?\n'))
game.run(iterations)

