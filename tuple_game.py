

# this import allows to "roll dice" by randomly selecting a number from die_faces
import random

# prints a welcome statement to the players of the game
print("Hello world and welcome to the Tuple Out Game!")

die_faces = (1, 2, 3, 4, 5, 6)

# functions to simulate each player's turn
def player1_turn():
    """Simulates one turn for 'Player 1' - rolls three different dice and assigns points according to the game's rules"""
    input("Player 1 turn. Press the 'enter' key on your keyboard to roll the three dice. \n")
    roll_results = []
    for dice_roll in range(3):
        this_roll = random.choice(die_faces)
        roll_results.append(this_roll)

    # if all three dice return the same value, you 'tupled out' and earn 0 points
    if roll_results[0] == roll_results[1] and roll_results[1] == roll_results[2]:
        print("You have 'tupled out' so you earned 0 points for this turn.")
        
    # if the outcome for two out of three dice are the same, those dice are fixed and cannot be re-rolled
    elif roll_results[0] == roll_results[1] or roll_results[0] == roll_results[2] or roll_results[1] == roll_results[2]:
        print("These two dice have the same value and are 'fixed'. They cannot be re-rolled")
        reroll_choice = input("Do you want to reroll the 'unfixed' die? If so, type 'y' or 'n' \n")
        # rerolls the 'unfixed' die if player wants to
        if reroll_choice == 'y':
            if roll_results[0] == roll_results[1] and roll_results[1] != roll_results[2]:
                reroll = random.choice(die_faces)
                player_points["Player 1"] += reroll + roll_results[0] * 2
            elif roll_results[1] == roll_results[2] and roll_results[1] != roll_results[0]:
                reroll = random.choice(die_faces)
                player_points["Player 1"] += reroll + roll_results[1] * 2
            elif roll_results[2] == roll_results[0] and roll_results[0] != roll_results[1]:
                reroll = random.choice(die_faces)
                player_points["Player 1"] += reroll + roll_results[2] * 2
        elif reroll_choice == 'n':
            print(f"Your turn has ended and these are your current points: {player_points}")
    else:
        player_points["Player 1"] += sum(roll_results)
    return print(f"Your turn has ended. These are the current points: {player_points}")

def player2_turn():
    """Simulates one turn for 'Player 2' - rolls three different dice and assigns points according to the game's rules"""
    input("Player 2 turn. Press the 'enter' key on your keyboard to roll the three dice. \n")
    roll_results = []
    for dice_roll in range(3):
        this_roll = random.choice(die_faces)
        roll_results.append(this_roll)

    # if all three dice return the same value, you 'tupled out' and earn 0 points
    if roll_results[0] == roll_results[1] and roll_results[1] == roll_results[2]:
        print("You have 'tupled out' so you earned 0 points for this turn.")
        
    # if the outcome for two out of three dice are the same, those dice are fixed and cannot be re-rolled
    elif roll_results[0] == roll_results[1] or roll_results[0] == roll_results[2] or roll_results[1] == roll_results[2]:
        print("These two dice have the same value and are 'fixed'. They cannot be re-rolled")
        reroll_choice = input("Do you want to reroll the 'unfixed' die? If so, type 'y' or 'n' \n")
        # rerolls the 'unfixed' die if player wants to
        if reroll_choice == 'y':
            if roll_results[0] == roll_results[1] and roll_results[1] != roll_results[2]:
                reroll = random.choice(die_faces)
                player_points["Player 2"] += reroll + roll_results[0] * 2
            elif roll_results[1] == roll_results[2] and roll_results[1] != roll_results[0]:
                reroll = random.choice(die_faces)
                player_points["Player 2"] += reroll + roll_results[1] * 2
            elif roll_results[2] == roll_results[0] and roll_results[0] != roll_results[1]:
                reroll = random.choice(die_faces)
                player_points["Player 2"] += reroll + roll_results[2] * 2
        elif reroll_choice == 'n':
            print(f"Your turn has ended and these are your current points: {player_points}")
    else:
        player_points["Player 2"] += sum(roll_results)
    return print(f"Your turn has ended. These are the current points: {player_points}")

def AI_turn():
    """Simulates one turn for 'AI' - rolls three different dice and assigns points according to the game's rules"""
    print("AI player turn")
    roll_results = []
    for dice_roll in range(3):
        this_roll = random.choice(die_faces)
        roll_results.append(this_roll)

    # if all three dice return the same value, you 'tupled out' and earn 0 points
    if roll_results[0] == roll_results[1] and roll_results[1] == roll_results[2]:
        print("AI has 'tupled out' so it earned 0 points for this turn.")
        
    # if the outcome for two out of three dice are the same, those dice are fixed and cannot be re-rolled
    elif roll_results[0] == roll_results[1] or roll_results[0] == roll_results[2] or roll_results[1] == roll_results[2]:
        player_points["AI"] += sum(roll_results)
        print("These two dice have the same value and are 'fixed'. They cannot be re-rolled. AI turn has ended.")
    else:
        player_points["AI"] += sum(roll_results)
    return print(f"AI's turn has ended. These are the current points: {player_points}")

def player3_turn():
    """Simulates one turn for 'Player 3' - rolls three different dice and assigns points according to the game's rules"""
    input("Player 3 turn. Press the 'enter' key on your keyboard to roll the three dice. \n")
    roll_results = []
    for dice_roll in range(3):
        this_roll = random.choice(die_faces)
        roll_results.append(this_roll)

    # if all three dice return the same value, you 'tupled out' and earn 0 points
    if roll_results[0] == roll_results[1] and roll_results[1] == roll_results[2]:
        print("You have 'tupled out' so you earned 0 points for this turn.")
        
    # if the outcome for two out of three dice are the same, those dice are fixed and cannot be re-rolled
    elif roll_results[0] == roll_results[1] or roll_results[0] == roll_results[2] or roll_results[1] == roll_results[2]:
        print("These two dice have the same value and are 'fixed'. They cannot be re-rolled")
        reroll_choice = input("Do you want to reroll the 'unfixed' die? If so, type 'y' or 'n' \n")
        # rerolls the 'unfixed' die if player wants to
        if reroll_choice == 'y':
            if roll_results[0] == roll_results[1] and roll_results[1] != roll_results[2]:
                reroll = random.choice(die_faces)
                player_points["Player 3"] += reroll + roll_results[0] * 2
            elif roll_results[1] == roll_results[2] and roll_results[1] != roll_results[0]:
                reroll = random.choice(die_faces)
                player_points["Player 3"] += reroll + roll_results[1] * 2
            elif roll_results[2] == roll_results[0] and roll_results[0] != roll_results[1]:
                reroll = random.choice(die_faces)
                player_points["Player 3"] += reroll + roll_results[2] * 2
        elif reroll_choice == 'n':
            print(f"Your turn has ended and these are your current points: {player_points}")
    else:
        player_points["Player 3"] += sum(roll_results)
    return print(f"Your turn has ended. These are the current points: {player_points}")

# test case 1 - tests the player1_turn() function
# player1_turn()

# test case 2 - tests the player2_turn() function
#player2_turn()

# asks how many players are playing the game 
player_count = input("How many players are playing? There is a maximum of 3 players. \n")

# executes the game, allows players to take turns, ends when a player reaches 50 points
if player_count == "1":
    play_ai = input("Would you like to play against an 'AI' player? Enter: y or n \n")
    if play_ai == 'y':
        player_points = {"Player 1" : 0, "AI" : 0}
        while player_points["Player 1"] < 50 or player_points["AI"] < 50:
            player1_turn()
            AI_turn()
            if player_points["Player 1"] >= 50:
                print(f"Congrats! You were first to earn 50 points and you won the game! These are your points: {player_points['Player 1']}")
                break
            elif player_points["AI"] >= 50:
                print(f"Unfortunately, the AI player has won by being first to earn 50 points. This is the total score: {player_points}")
                break
    elif play_ai == 'n':
        player_points = {"Player 1" : 0}
        while player_points["Player 1"] < 50:
            player1_turn()
            if player_points["Player 1"] >= 50:
                print(f"Congrats! You earned 50 points and you won the game! These are your points: {player_points['Player 1']}")
                break
elif player_count == "2":
    player_points = {"Player 1" : 0, "Player 2" : 0}
    while player_points["Player 1"] < 50 or player_points["Player 2"] < 50:
        player1_turn()
        player2_turn()
        if player_points["Player 1"] >= 50:
            print(f"Congrats Player 1! You were first to earn 50 points and you won the game! These are your points: {player_points['Player 1']}")
            break
        elif player_points["Player 2"] >= 50:
            print(f"Congrats Player 2! You were first to earn 50 points and you won the game! These are your points: {player_points['Player 2']}")
            break
elif player_count == "3":
    player_points = {"Player 1" : 0, "Player 2" : 0, "Player 3" : 0}
    while player_points["Player 1"] < 50 or player_points["Player 2"] < 50 or player_points["Player 3"] < 50:
        player1_turn()
        player2_turn()
        player3_turn()
        if player_points["Player 1"] >= 50:
            print(f"Congrats Player 1! You were first to earn 50 points and you won the game! These are your points: {player_points['Player 1']}")
            break
        elif player_points["Player 2"] >= 50:
            print(f"Congrats Player 2! You were first to earn 50 points and you won the game! These are your points: {player_points['Player 2']}")
            break
        elif player_points["Player 3"] >= 50:
            print(f"Congrats Player 3! You were first to earn 50 points and you won the game! These are your points: {player_points['Player 3']}")
            break

# adds final scores to a 'results' document
message = f"""These are the final points for each player from the tuple game: {player_points}\n"""
with open("tuple_game_results.txt", "a") as output_connection:
    output_connection.write(message)




