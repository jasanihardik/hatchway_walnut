lst = []
d = dict()
user = input("enter a string ::-- ")
lst = user.split(',')
print("LIST ELEMENT ARE :: ", lst)
l = len(lst)
for i in range(l):
    c = 0
    for j in range(l):
        if lst[i] == lst[j]:
            c += 1
    d[lst[i]] = c
print("dictionary is  :: ", d)
