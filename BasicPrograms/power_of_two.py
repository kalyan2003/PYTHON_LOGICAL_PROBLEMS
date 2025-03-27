num = int(input("Enter the number to find powers till the taken number :"))

def calculating_poweroftwo(num):
  """
  Calculates the power 2 table till the number that was taken as argument

  Arguments : num (int)

  will return power of 2 for the given value.

  """
  return f"power of 2 power {num} is {pow(num,2)}"


if(num>=31):
  print("overflow pls take value less than 31")
else:
  for i in range(num):
    print(calculating_poweroftwo(i))



