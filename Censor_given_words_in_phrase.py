# Write a script to read a string and censor any word from a given list. Every character of the removed word must be replaced by "*".

string = "Matthew has a fat ass"
list = ["ass"]

ind_words = string.split()

for words in ind_words:
    for i in list:
        if i == words:
            string = string.replace(words, "*" * len(words))

print(string)
