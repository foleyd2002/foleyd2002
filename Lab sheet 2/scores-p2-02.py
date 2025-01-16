input_scores = input("Please enter a comma-separated list of scores:")
if ',' not in input_scores:
    print("The list of scores is not valid.")
    exit()

scores_strings = input_scores.split(',')
scores = []
for number in scores_strings:
    scores.append(int(number))


wins = 0
draws = 0
losses = 0
wrong_element_counter = 0

for element in scores:
    if element == 3:
        wins = wins + 1
    elif element == 1:
        draws = draws + 1
    elif element == 0:
        losses = losses + 1
    else:
        wrong_element_counter = wrong_element_counter + 1

if wrong_element_counter == 0:
    print(f"Draws: {draws}")
    print(f"Losses: {losses}")
    print(f"Wins: {wins}")
else:
    print("The list of scores is not valid.")