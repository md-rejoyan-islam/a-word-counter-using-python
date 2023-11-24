import re
# search words
search_words =["java","Python","C++","go","javascript","sql","nodemon","react"]

# read txt file
with open("./file.txt","r") as file:
    data = file.read()

    # match words
    for word in search_words:
        matches = re.findall(rf"\b{word}\b",data,flags=re.IGNORECASE)
        print(f"{word} : {len(matches)}")
