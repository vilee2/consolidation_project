
# this import allows to "roll dice" by randomly selecting a number from die_faces
import random

# asks how many players are playing the game
player_count = input("How many players are playing?\n")
print(player_count)

if player_count == 1:
    player_points = {"Player 1" : 0}
elif player_count == 2:
    player_points = {"Player 1" : 0, "Player 2" : 0}
elif player_count == 3:
    player_points = {"Player 1" : 0, "Player 2" : 0, "Player 3" : 0}

die1 = (1, 2, 3, 4, 5, 6)
die2 = (1, 2, 3, 4, 5, 6)
die3 = (1, 2, 3, 4, 5, 6)

roll_results = []
roll_counts = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0} 

def dice_roll():
    for face in range(1):
        outcome_die1 = random.choice(die1)
        outcome_die2 = random.choice(die2)
        outcome_die3 = random.choice(die3)
    if outcome_die1 == outcome_die2 and outcome_die2 == outcome_die3:
        points = 0
        player_points[points] == 0
        print("You have 'tupled out' so you have 0 points for this turn.")
    elif outcome_die1 == outcome_die2 or outcome_die1 == outcome_die3 or outcome_die2 == outcome_die3:
        print("These two dice have the same value and are 'fixed'. They cannot be re-rolled")







