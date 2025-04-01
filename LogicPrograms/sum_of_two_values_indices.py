arr = []
n = int(input())
target = int(input())

for i in range(n):
    arr.append(int(input()))

map_dict = {}
indi = []
for i in range(n):
    rem = target - arr[i]
    if rem in map_dict:
        indi.append(map_dict[rem])
        indi.append(i)
        break

    map_dict[arr[i]] = i


print(indi)



