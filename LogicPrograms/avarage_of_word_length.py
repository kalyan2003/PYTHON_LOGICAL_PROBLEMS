str = input()

spec_count = 0
space_count = 0
char_count = 0


for i in range (len(str)):
    if str[i].isalnum():
        char_count += 1
    elif not str[i].isalnum() and str[i] != ' ':
        spec_count += 1
    elif str[i] == ' ':
        space_count += 1

space_count += 1

print(char_count)
print(space_count)
print(f"{char_count / space_count:.2f}")


