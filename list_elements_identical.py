# Write a script that takes a list and returns True if all elements in the list are identical, and False otherwise

list = ["SS", "SS", "SS", "SS"]

list_elements = set(list)

if len(list_elements) == 1:
    print("True")
else:
    print("False")
