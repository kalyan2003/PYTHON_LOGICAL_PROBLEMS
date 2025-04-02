num = int(input("Length of array"))

arr = []

for i in range(num):
    arr.append(int(input()))


def reverse_the_array(arr,num):
    i = 0
    j = num-1

    while(i<j):
        arr[i],arr[j] = arr[j],arr[i]

        i += 1
        j -= 1

    return arr

print(reverse_the_array(arr,num))

