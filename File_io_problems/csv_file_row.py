import csv

file = open("username-password-recovery-code.csv", "r")
file1 = open("output_file.txt", "w")

read = csv.reader(file)
csv_data = list(read)

col_num = int(input("Enter the column number: ")) - 1


if 0 <= col_num < len(csv_data[0]):
    for row in csv_data:
        if len(row) > col_num:
            file1.write(str(row[col_num]) + "\n")

    print("Data extracted successfully")
else:
    print("Invalid column number!")

file.close()
file1.close()
