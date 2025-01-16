scores_input = input("Please enter a comma-separated list of scores:")

# Check if the input is a valid comma-separated list of integers
if all(score.strip().isdigit() and int(score.strip()) in {0, 1, 3} for score in scores_input.split(',')):
    scores = [int(score) for score in scores_input.split(',')]

    wins = scores.count(3)
    draws = scores.count(1)
    losses = scores.count(0)

    print(f"Draws: {draws}")
    print(f"Losses: {losses}")
    print(f"Wins: {wins}")

else:
    print(f"Draws: 0")
    print(f"Losses: 0")
    print(f"Wins: 0")


