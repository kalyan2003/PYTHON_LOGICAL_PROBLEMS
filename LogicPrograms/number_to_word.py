def number_to_words(num):
    if num == 0:
        return "Zero"

    ones = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
        8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
        14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
        19: "Nineteen"
    }

    tens = {
        20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy",
        80: "Eighty", 90: "Ninety"
    }

    if num in ones:
        return ones[num]

    if num in tens:
        return tens[num]

    if num < 100:
        tens_part = tens[num // 10 * 10]
        ones_part = ""
        if num % 10 != 0:
            ones_part = ones[num % 10]
        if ones_part:
            return tens_part + " " + ones_part
        return tens_part

    if num < 1000:
        hundreds_part = ones[num // 100] + " Hundred"
        remainder_part = ""
        if num % 100 != 0:
            remainder_part = number_to_words(num % 100)
        if remainder_part:
            return hundreds_part + " " + remainder_part
        return hundreds_part

    if num == 1000:
        return "One Thousand"

    return ""



num = int(input("Enter a number: "))

print(number_to_words(num))
