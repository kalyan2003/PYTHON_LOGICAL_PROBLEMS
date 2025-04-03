file = open("my_file.txt","r")
text = file.read()
file.close()

text = "".join(reversed(text))

file = open("output_file.txt","w")
file.write(text)
file.close()