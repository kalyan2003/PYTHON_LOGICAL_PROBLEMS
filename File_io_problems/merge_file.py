file1 = open("my_file.txt","r")
file2 = open("output_file.txt","r")

file3 = open("output_file2.txt","w")

while True:
    line1 = file1.readline()
    line2 = file2.readline()

    if line1 != "" and line2 != "":
        file3.write(line1 +"\n")
        file3.write(line2 + "\n")

    elif line1 == "" and line2 != "":
        file3.write(line2)
        file3.write("\n")
    elif line1 != "" and line2 == "":
        file3.write(line1 + "\n")
    else:
        break

file1.close()
file2.close()
file3.close()