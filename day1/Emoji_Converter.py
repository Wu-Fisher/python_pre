message = input(">")

words =message.split(' ')
emojis= {
    ":)":"😊",
    ":(":"😭",
    "..":"🤤"
}
output=""
for word in words:
    output+=emojis.get(word,word)
    output+= " "
print(output)