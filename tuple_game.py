
import random

# asks how many players are playing the game
player_count = input("How many players are playing?\n")
print(player_count)

if player_count == 1:
    points = {"Player 1" : 0}
elif player_count == 2:
    points = {"Player 1" : 0, "Player 2" : 0}
elif player_count == 3:
    points = {"Player 1" : 0, "Player 2" : 0, "Player 3" : 0}

die_faces = (1, 2, 3, 4, 5, 6)


roll_results = []
roll_counts = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0} 
for face in range(3):
    this_roll = random.choice(die_faces)
    roll_results.append(this_roll)
    roll_counts[this_roll] += 1
print(roll_counts)





