## Sorting the dictionary in ascending and descending order
my_dict = {
    "a":1,
    "b":3,
    "c":2,
    "d":5
}

asc_sort = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Sorted in ascending order",asc_sort)

desc_sort = dict(sorted(my_dict.items(), key=lambda item: item[1] , reverse=True))

print("Sorted in descending order",desc_sort)


## Updating the dictionary by adding another key

my_dict = {
      "0":10,
      "1":20
}

my_dict.update({"2":30})

print("Updated dictionary:", my_dict)


## Append the three dic into one dic

dic1 = {1:10,2:20}
dic2 = {3:30,4:40}
dic3 = {5:50,6:60}

dic4 = {}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)

print("Final appended dictionary:",dic4)

##To iterate over dictionaries

main_dict = {
    "dic1": {1: 10, 2: 20},
    "dic2": {3: 30, 4: 40},
    "dic3": {5: 50, 6: 60}
}

for x, dic in main_dict.items():
    print(x)

    for y in dic:
        print(y, ":", dic[y])

## Create a new dictionary with in the given range from i to n

dict = {}

num = int(input())

for i in range(1,num+1):
    key = i
    value = i*i
    dict[key] = value

print ("Final dictionary is ", dict)

## To remove the key from dictionary

dict = {
    "car":"mustang",
    "model":1,
    "year":2009
}

dict.pop("model")
print("Updated dictionary after deletion:", dict)

## Python program to print all unique values from multiple dictionaries

dict_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
             {"VIII": "S007"}]

mapped = set()

for dict in dict_list:
    for value in dict:
        mapped.add(dict[value])

print("UNIQUE VALUES :")
print(mapped)

## Finding the frequency of each char in string w3schools and store in the form of dictionary
str = "w3resource"

my_dict = {}

for i in range(len(str)):
    ch = str[i]
    count_freq  = str.count(ch)
    my_dict[ch] = count_freq

print(my_dict)

##Print the dictionary in table format
my_dict = {
    1: ["pavan", 21, 'python'],
    2: ["kalyan", 22, 'sql'],
    3: ["chimmiri", 23, 'java'],
}

print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))

for key, value in my_dict.items():
    name, age, course = value
    print("{:<10} {:<10} {:<10}".format(name, age, course))

