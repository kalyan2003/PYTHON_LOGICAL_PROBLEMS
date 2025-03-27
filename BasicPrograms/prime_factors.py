
#function starts here

def prime_factors(n):
    """
    Computes the prime factorization of N .

    Arguments : n

    Will return the prime factorization
    """

    if n <= 1:
        print("Enter a number greater than 1")
        return

    print(f"Prime factors of {n} are:", end=" ")

    
    while n % 2 == 0:
        print(2,end=" ")
        n //= 2

    
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            print(factor, end=" ")
            n //= factor
        factor += 2  

   
    if n > 1:
        print(n, end=" ")

#function ends here

num = int(input("Enter a number to find its prime factors: "))
prime_factors(num)

