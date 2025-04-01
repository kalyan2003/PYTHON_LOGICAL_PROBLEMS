dic1 = {
    'a': 1,
    'b': 2,
    'c': 2,
    'e': 3
}

dic2 = {}
lst = []
for key in dic1:
    ele = dic1[key]

    dic2.setdefault(ele, []).append(key)


dic3 = {}
for key in dic2:
    lst = dic2[key]

    for ele in lst:
        dic3[ele] = key

print(dic3)
