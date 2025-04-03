## Implementing the dictionary comprehensions

year_nums = [x for x in range(1,4)]
year = ["jan","feb","mar"]

dic_list = {num: month for num,month in zip(year_nums,year)}

print(dic_list)

##List Comprehensions
eve_list = [x for x in range(0,12,2)]
print(eve_list)
odd_list = [x+1 if x%2!=0 else x for x in eve_list]
print(odd_list)

## Set Comprehensions
eve_list = {x for x in range(0,12,2)}
print(eve_list)