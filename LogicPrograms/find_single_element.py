def find_single_ele(arr):
    sorted_arr = sorted(arr)
    ele_single = 0
    for i in range(0,len(arr)):
        if i == 0:
            if sorted_arr[i] != arr[i+1]:
                ele_single = sorted_arr[i]
                break
        elif i != len(arr)-1:
            if sorted_arr[i] != sorted_arr[i+1] and sorted_arr[i] != sorted_arr[i-1]:
                ele_single = sorted_arr[i]
                break
        else:
            if sorted_arr[i] != sorted_arr[i-1]:
                ele_single = arr[i]
                break

    return ele_single


arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))


single_element = find_single_ele(arr)
print(single_element)