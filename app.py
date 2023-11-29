import re
# search words
search_words =["Java","Python","C++","go","javascript","sQl","nodemon","ReAct"]

# read txt file
with open("./file.txt","r") as file:
    data = file.read()

    # match words
    for word in search_words:
        matches = re.findall(rf"\b{word.lower()}\b",data,flags=re.IGNORECASE)
        print(f"{word} : {len(matches)}")
