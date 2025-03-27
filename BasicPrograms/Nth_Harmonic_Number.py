num = int(input("Enter the number to find the nth harmonic number :"))

def cal_nth_Harmonic(num):
  """
  Calculating the nth harmonic number 
  
  Arguments :  num (int)

  The function will return the nth harmonic number .
  """

  sum=0
  for i in range(1,num+1):
    sum = sum + (1/i);

  return sum

print(cal_nth_Harmonic(num))


