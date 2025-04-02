arr = []

n = int(input())

ri = 0
li = -1
for i in range(n):
    arr.append(int(input()))


for i in range(n):
    if arr[i] == 0:
        li = i
        break


for ri in range(n):
    if arr[ri] != 0 and ri > li:
        arr[ri], arr[li] = arr[li], arr[ri]
        li += 1

print(*arr)
