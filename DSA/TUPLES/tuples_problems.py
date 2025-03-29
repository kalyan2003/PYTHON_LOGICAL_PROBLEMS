#Progrm to create a simple tuple

mt_tuple = ("1","2")

print(mt_tuple)

#Creating tuple with multiple data types

mt_tuple = ("1",3,True,"pavan",9.86)

print(mt_tuple)

# Unpacking the tuple
mt_tuple = ("a","b","c")

(d,e,f)  = mt_tuple

print(d)
print(e)
print(f)

##Implement the colon of a tuple
from copy import deepcopy

mt_tuple = ("a","b","c",[10])

nt_tuple = deepcopy(mt_tuple)

nt_tuple[3].append(50)
print(nt_tuple)
print(mt_tuple)

## Find the repeated elements in the tuple
mt_tuple = ("a", "b", "c", "a")

ts_lst = []

for i in mt_tuple:
    if i not in ts_lst:
        ts_lst.append(i)
    else:
        print(i)

##To find whether a given element is in tuple
mt_tuple = ("a","b","c","a")

st = "a"

if st in mt_tuple:
    print (True)
else:
    print (False)

##Convert a list into a tuple

mt_list = ["a","b","c","a"]

mt_tuple = tuple(mt_list)

print(mt_tuple)

## Remove elements from an tuple
mt_tuple = ("a","b","c","a")

ls = list(mt_tuple)

ls.remove("a")

mt_tuple = tuple(ls)

print(mt_tuple)

##Slicing the tuple
mt_tuple = ("a","b","c","a")

print(mt_tuple[1:3])

##Reverse a tuple
mt_tuple = ("a","b","c","a")

mt_tuple = tuple(reversed(mt_tuple))
print(mt_tuple)

