import random

 ###function starts here

def cal_Head_Tail_percentage(num):
  """
  Calculating the head and tails percentage by flipping the coin few times 

  Arguments :  num (int)

  Function will return the percentage of heads and percentage of tails will come for the given number
  """

  if num<=0 :
    print("Enter a value which is greater than 0")
    return
  

  heads = 0
  tails = 0

  for _ in range(num):
    toss_Result = random.random()

    if(toss_Result<0.5):
      tails = tails+1
    else :
      heads = heads+1


  return((heads/num) * 100,(tails/num) * 100)

  ###function ends here



num = int(input("Enter the number of times the coin should flip :"))



heads_percentage,tails_percentage = cal_Head_Tail_percentage(num)

print(f"Heads percentage: {heads_percentage:.2f}%")
print(f"tails percentage: {tails_percentage:.2f}%")