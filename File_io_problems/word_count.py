
file = open("my_file.txt","r")

text = file.read()

file.close()

text = text.lower()

punct = ".,!?;:'\"()-[]{}"
for p in punct:
    text = text.replace(p,"")

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


file = open("output_file.txt","w")

for word in word_count:
    file.write(word + ":" + str(word_count[word]) + "\n")

file.close()