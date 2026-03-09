# initialise list to hold game history
game_history = []

# get data (base component does thi already, code for testing purposes)


while True:
    rounds_played = input("Round?")
    if rounds_played == "":
        break

    user_points = int(input("user points?"))
    comp_points = int(input("computer points?"))
    winner = input("who won?")
    user_score = int(input("user score:"))
    comp_score = int(input("computer score:"))

    game_results = (f"Rounds {rounds_played}: User points {user_points} |"
                    f" computer points {comp_points}, {winner} wins (15 | 0"
                    f"({user_score} | {comp_score})")

    game_history.append(game_results)

print("game history")

for item in game_history:
    print(item)


