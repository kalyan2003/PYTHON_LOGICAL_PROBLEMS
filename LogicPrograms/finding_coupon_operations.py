import random

class CouponProcessor:
    @staticmethod
    def generate_random(numbers):
        """
        Generates a random number from the given list.

        Arguments : numbers (int)

        will return a random number from the taken choices from the above numbers list
        """
        return random.choice(numbers)

    @staticmethod
    def process_coupons(numbers):
        """
        Processes distinct coupons until all numbers are mapped.

        Arguments : numbers (int)

        Return the how many times the random function executes . 
        """
        mapped = set()
        count = 0

        while len(mapped) < len(numbers):
            rand_num = CouponProcessor.generate_random(numbers)
            mapped.add(rand_num)
            count += 1

        return count



numbers = list(map(int, input("Enter the numbers separated by space: ").split()))
execution_count = CouponProcessor.process_coupons(numbers)

print("Total random function executions:", execution_count)

