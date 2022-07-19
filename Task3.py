word = str(input("type a word or phrase"))
count = 0
for letter in list(word):

    if (letter.isalpha()):
        count+=1

print("There are "+str(count)+" letters in " + word)

