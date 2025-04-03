
file1 = open("my_file.txt","r")
lines1 = file1.readlines()

file2 = open("output_file2.txt","r")
lines2 = file2.readlines()

file3 = open("output_file.txt","w")

line_len = max(len(lines1),len(lines2))

for i in range(line_len):
    if i < len(lines1):
        sin_line1 = lines1[i]
    else:
        "EOF"

    if i<len(lines2):
        sin_line2 = lines2[i]
    else:
        "EOF"

    if sin_line2 != sin_line1:
        file3.write(f"Difference at line {i+1}\n")
        file3.write(f"File1 : {sin_line1}\n")
        file3.write(f"File2 : {sin_line2}\n\n")

file3.close()
file1.close()
file2.close()

