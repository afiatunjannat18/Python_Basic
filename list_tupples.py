a = [1,2,3,'Naim','Fahim', 8,9,3,4]

 #list mutable

a[0]=100
print(a)
print(len(a))

a.append([1,2,3])
print(a)

a.reverse()
print(a)

#tuple immutable
t=(1,2,3)
t_r=tuple(reversed(t))
print(t)
print(t_r)

s='Hello'
print(list(s))


