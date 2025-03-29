## Program to sum the elements in the list

my_set = []
length = int(input("Enter the length: "))

for i in range(length):
    my_set.append(int(input()))

def sum_list(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total

print(sum_list(my_set))

## Program to multiply the elements in the list

my_set = []
length = int(input("Enter the length: "))

for i in range(length):
    my_set.append(int(input()))

def multiply_list(lst):
    total = 1
    for i in range(len(lst)):
        total *= lst[i]
    return total

print(multiply_list(my_set))

## Program to find the minimum from the list

my_list = []
length = int(input("Enter the length: "))

for i in range(length):
    my_list.append(int(input()))

def minimum_lst(lst):
    return min(lst)
print(minimum_lst(my_list))

##Program to count the num of strs based on the conditions

my_list = ["abc", "xyz", "aba", "1221"]


def count_freq_str(my_list):
    count = 0

    for i in range(len(my_list)):
        st = my_list[i]
        st_len = len(my_list[i])

        if len(st) > 2:
            if st[0] == st[st_len - 1]:
                count += 1

    return count


print(count_freq_str(my_list))

## Sorting the tuples in the list based on element 2
my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

n = len(my_list)

for i in range(n):
    for j in range(0, n - i - 1):
        if my_list[j][1] > my_list[j + 1][1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print(my_list)

##Removing the duplicates from the list
my_list = [1, 2, 3, 4, 5, 5, 4, 3]

unique_list = []

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)


## Cloning the list
my_list = [1,2,3,4,5,5,4,3]

unique_list = []

unique_list = my_list[:]

print(unique_list)


## Find the list of words that are greater than n
my_list = ["pavan", "kalyan", "varun", "bridzelabz"]

new_list = []

n = 6

for i in range(len(my_list)):
    if len(my_list[i]) > n:
        new_list.append(my_list[i])

print(new_list)

## Comparing two lists if words are present in both then return true else return false
my_list = ["pavan", "kalyan", "varun", "bridzelabz"]

new_list = ["pavan", "kalyan"]


def common_word_in_lists(lst1, lst2):
    for word in my_list:
        if word in new_list:
            return True

    return False


print(common_word_in_lists(my_list, new_list))

## Removing the elements from the list based on the given index

my_list = ['Red','green','white','black','pink','yellow']

my_list.remove(my_list[5])
my_list.remove(my_list[4])
my_list.remove(my_list[0])

print(my_list)

##Finding the all permutations of the list

my_list = ['Red','green','white','black','pink','yellow']

my_list.remove(my_list[5])
my_list.remove(my_list[4])
my_list.remove(my_list[0])

print(my_list)

## Removing duplicates in the list of the lists

my_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

new_list = []

for sub_lst in my_list:
    if sub_lst not in new_list:
        new_list.append(sub_lst)

print(new_list)

