year = int(input("Enter the year to find it a leap year or non leap year :"))

def find_leap_year_ornot(year):
  """ 
  Finding wheather a year is leap year or non leap year 

  Arguments : year (int)

  result: Function will return wetather it is leap year or non leap year

  """

  if(year%4==0 and year%100==0 and year%400==0):
    return "The given year is a leap year"
  else:
    return "The given year is not a leap year"

print (find_leap_year_ornot(year))