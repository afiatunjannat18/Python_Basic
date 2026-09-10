a=[1,2,3,4,"a",5,6,7]

print(type('b'))
for i in a:
    if type(i) == type('b'):
        break
    else:
        print(i)

for i in a:
    if type(i) == type('a'):
        continue
    else:
        print(i)