file = open("my_file.txt","r")

while True:
    data_chunk = file.read(1024)

    if not data_chunk:
        break


    print(data_chunk)

file.close()
