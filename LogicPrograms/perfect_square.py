num = int(input("Enter a number: "))

def check_for_perfect_square(num):

    i = 1

    while i*i <= num:
        if i*i == num:
            return True

        i = i+1

    return False


print(check_for_perfect_square(num))