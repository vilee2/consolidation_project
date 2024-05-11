# Tuple Out Dice Game

## Rules to the Game:
Players score points by rolling dice. 
The goal of the game is to be the first to reach 50 points. The game will end when a player reaches 50 points. 
The active player rolls three dice. 
    If all three dice are rolled with same number, player "tupled out" and gets 0 points for that turn. 
    If two dice have same number, they cannot be re-rolled and are considered "fixed".
    Player can re-roll dice that are not "fixed".
The player's points is equal to total of the three dice and their turn ends, unless they 'tupled out'. 


## How the Game Works:
The game begins by asking how many players are playing the game. User will input a number from 1 to 3. 
    There is a maximum of three players that can play this game. 
    If only one person is playing, they can choose to play against an AI player. The AI player will choose not to re-roll dice when there are 'fixed' dice. 
At the beginning of a player's turn, the player presses "enter" on their keyboard to roll the dice during their turn.
If all three dice are rolled to get the same number, player "tupled out" and gets 0 points for that turn. Their turn ends. 
If two dice have same number, they cannot be re-rolled and are considered "fixed". 
The game will ask if the player wants to re-roll the die that is not "fixed". The game will re-roll the die and add up the current points. The turn ends.
The current scores are displayed at the end of each player's turn. 
The game will move on to the next player's turn and follow the above procedure. 
The game continues until a player reaches 50 points. That player wins the game and the game ends.

## The Game Can...:
The game can ask how many players are playing the game.
The game can have players take turns rolling dice.
The game can have players press 'enter' on their keyboard as an interactive way to roll the dice.
The game has the option for a single player to play against an AI player.
The game can display the running scores, so that players know what the current scores are. 
The game can record the scores of each player at the end of the game and write it to a results text file. 
The game can record the wins of each player at the end of the game and write it to a results text file. 
The game can use pandas and matplotlib to create a data frame and create a bar graph of the players' scores. 

## Limitations of the Game:
The game cannot have more than three players.
Aside from re-rolling a die that is 'unfixed', players cannot re-roll a die. 
When re-rolling a die that is 'unfixed', players cannot keep re-rolling the die. (Players can only re-roll an 'unfixed' die once.)
The game cannot record high score records. 
The game cannot change the dice.
There is no special scoring. 

