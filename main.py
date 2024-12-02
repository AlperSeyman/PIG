import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll


while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
            
    else:
        print("Invalid, try again")
max_score = 40
players_score = []

for _ in range(players):
    players_score.append(0)

while max(players_score) < max_score:
    for player in range(players):
        print(f"\nPlayer {player + 1} turn just started!")
        print(f"Your Total Score : {players_score[player]}\n")
        current_score = 0
        while True:
            should_roll = input("Do you want to roll (y) ? ")
            if should_roll.lower() != "y":
                break
        
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!.")
                current_score = 0
                break
            else:
                current_score = current_score + value
                print(f"You rolled a: {value}")

            print(f"Your current score : {current_score}")

        players_score[player] = players_score[player] + current_score
        print(f"Your total score is {players_score[player]}")

max_Score = max(players_score)
for player, score in enumerate(players_score):
    print(f"Player {player + 1} ---> {score}")


for player, score in enumerate(players_score):
    if score == max_Score:
        print(f"Player {player + 1} has the highest {score} score")
        break
