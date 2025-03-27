
name = input("what is your name ?")

###Function starts here

def greet_msg(name):
  
  """
  Taking name of the from the user and greeting the user

  Arguments : name (int)

  will return a greet message
  """
  if(len(name)>3) :
      return "Hello "+name+",how are you ?"
  else:
     return "Length of the name is smaller than 3 characters ."
  
  ###Function ends here

print(greet_msg(name))

