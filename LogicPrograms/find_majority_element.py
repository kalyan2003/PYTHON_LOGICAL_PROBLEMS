
def find_majority_elem(arr):
    my_map = {}

    for i in range(len(arr)):
        if arr[i] in my_map:
            my_map[arr[i]] += 1
        else:
            my_map[arr[i]] = 1

    for element in my_map:
        if my_map[element] > len(arr)//2:
            return element

    return -1


arr = []

n = int(input())

for i in range(n):
    arr.append(int(input()))

print(find_majority_elem(arr))