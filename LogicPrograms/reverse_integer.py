num_copy = int(input())

if num_copy <0 :
    num = -1*num_copy
else:
    num = num_copy

rev_num = 0
while num > 0:
    rem = num%10
    rev_num = rev_num * 10 + rem
    num = num // 10

if num_copy <0 :
    rev_num = -1 * rev_num
    print(rev_num)
else :
    print(rev_num)

