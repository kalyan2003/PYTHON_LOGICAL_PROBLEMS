
## DISPLAY ARRAY ITEMS

arr = []

for i in range(5):
    arr.append(int(input()))
print("Accessing the elements through index values :")
for i in range(5):
    print(arr[i])


## COUNT NUMBER OF OCCURRENCE OF ELEMENT

arr = []
k = int(input())

count = 0
for i in range(5):
    arr.append(int(input()))

for i in range(len(arr)):
    if arr[i] == k:
        count += 1

print(f"the Occurences of {k} are : {count}")


## Reverse an array

arr = []

for i in range(5):
    arr.append(int(input()))

arr.reverse()

for i in range(len(arr)):
    print(arr[i])

## REMOVE THE FIRST OCCURENCE OF THE ELEMENT

arr = []

for i in range(5):
    arr.append(int(input()))

print("Enter the element to remove:")
k = int(input())

if k in arr :
    arr.remove(k)

print("Updated array:", arr)