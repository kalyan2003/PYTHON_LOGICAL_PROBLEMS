#create a set

my_set = {"pavan","kalyan",21}

print(my_set)

##iteration over the sets

my_set = {"pavan","kalyan",20}

for x in my_set:
    print(x)


##Program to add members in the set

my_set = {"pavan","kalyan",20}

my_set.add("chimmiri")

print(my_set)

##Program to remove item from the set

my_set = {"pavan","kalyan","chimmiri",20}
my_set.remove("chimmiri")
print(my_set)

##Python to remove an item it present in the set

my_set = {"pavan","kalyan","chimmiri",20}

item = "chimmiri"
if item in my_set:
   my_set.remove(item)
else:
    none
print(my_set)

##Intersection of sets
my_set = {"pavan","kalyan","chimmiri",20}

fr_set = {"pavan","kalyan",20}

set3 = my_set.intersection(fr_set)

print(set3)


## Union of sets
my_set = {"pavan","kalyan","chimmiri",20}

fr_set = {"pavan","kalyan",20}

set3 = my_set.union(fr_set)

print(set3)

## Difference of sets

my_set = {"pavan","kalyan","chimmiri",20}

fr_set = {"pavan","kalyan",20}

set3 = my_set - fr_set

print(set3)

## Symmetric difference of sets

my_set = {"pavan","kalyan","chimmiri",20}

fr_set = {"pavan","kalyan",20,30}

set3 = my_set.symmetric_difference(fr_set)

print(set3)


## Program to clear the set

my_set = {"pavan","kalyan","chimmiri",20}

my_set.clear()

print(my_set)

## Implementing Frozenset

my_set = frozenset(["pavan","kalyan","chimmiri",20])

print(my_set)

## Finding maximum and minimum elements in set

my_set = {1, 20, 40, 30, 10}


def find_max_min(my_set):
    maxi = max(my_set)
    mini = min(my_set)

    return (maxi, mini)

maximum, minimum = find_max_min(my_set)
print(maximum, "and", minimum)

