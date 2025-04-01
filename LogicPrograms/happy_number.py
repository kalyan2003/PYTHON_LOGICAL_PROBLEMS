n = int(input())

pre_set = set()

def find_num_is_happy(n,pre_set):
    if n == 1:
        return True

    if n in pre_set:
        return False

    pre_set.add(n)
    sum_of_squ = 0
    while n>0:
        rem = n%10

        sum_of_squ = sum_of_squ + rem*rem

        n = n//10

    return find_num_is_happy(sum_of_squ,pre_set)

print(find_num_is_happy(n,pre_set))
