
file = open("../Working_With_Modules/my_file.txt", "r")

data = file.read()

if "kalyan" in data:
    data = data.replace("kalyan","krishna")
    file1 = open("../Working_With_Modules/my_file.txt", "w")
    file1.write(data)
    file1.close()
else:
    print("The word is not existing")

