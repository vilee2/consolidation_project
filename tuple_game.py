
# this import allows to "roll dice" by randomly selecting a number from die_faces
import random
import numpy as np

# asks how many players are playing the game
# player_count = input("How many players are playing?\n")


player_points = {"Player 1" : 0}

die_faces = (1, 2, 3, 4, 5, 6)

roll_results = []
roll_counts = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0} 


def dice_roll(player):
    """rolls three different dice and assigns points according to the game's rules"""
    for dice_roll in range(3):
        this_roll = random.choice(die_faces)
        roll_results.append(this_roll)
        roll_counts[this_roll] += 1

    # if all three dice return the same value, you 'tupled out' and earn 0 points
    if roll_results[0] == roll_results[1] and roll_results[1] == roll_results[2]:
        print("You have 'tupled out' so you earned 0 points for this turn.")
        
    # if the outcome for two out of three dice are the same, those dice are fixed and cannot be re-rolled
    elif roll_results[0] == roll_results[1] or roll_results[0] == roll_results[2] or roll_results[1] == roll_results[2]:
        print("These two dice have the same value and are 'fixed'. They cannot be re-rolled")
        if roll_results[0] == roll_results[1] and roll_results[1] != roll_results[2]:
            reroll = random.choice(die_faces)
            player_points[reroll] += reroll + roll_results[0] * 2
        elif roll_results[1] == roll_results[2] and roll_results[1] != roll_results[0]:
            reroll = random.choice(die_faces)
            player_points[reroll] += reroll + roll_results[1] * 2
        elif roll_results[2] == roll_results[0] and roll_results[0] != roll_results[1]:
            reroll = random.choice(die_faces)
            player_points[reroll] += reroll + roll_results[2] * 2
    else:
        player_points["Player 1"] += sum(roll_results)
    return print(f"These are the current points: {player_points}")








