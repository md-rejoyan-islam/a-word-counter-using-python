import re
# search words
search_words = ["Java", "Python", "c++", "go",
                "javascript", "sql", "nodemon", "ReAct", "c#", "php"]

# read txt file
with open("./file.txt", "r") as file:
    data = file.read()

# file data as list
data = data.split("\n")

# remove empty string from list
data = list(filter(None, data))

# convert list items as lower case
data = [item.lower().strip() for item in data]


# match full word with case insensitive anc count
for word in search_words:
    match = data.count(word.lower())
    print(f"{word} : {match}")
