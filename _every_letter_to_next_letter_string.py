# Write a script to read a string and change every letter to the next letter

word = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
output_word = ""

for char in word:
    output_word += alphabet[alphabet.index(char) + 1]

print(output_word)