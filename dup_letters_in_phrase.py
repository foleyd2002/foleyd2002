# Given a phrase, return false if an individual word contains duplicate letters, true if otherwise

phrase = input()

split_phrase = phrase.split()

for word in split_phrase:
    