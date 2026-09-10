#{}
#key value pair
#indexing er sujogb nei
#key gulo immutable

a={'rahim': 12, 'Karim':14, 'Fahim': 78, 1:[1,2,3,4], 2:[2,3,4]}
print(type(a))
for i in a:
    print(i)

print("-----")
for i in a.values():
    print(i)
print(a.keys(), a.values())

print("----")
for k,v in a.items():
    print(f"key Name : {k}, values{v}")

print("-----")
a=[1,2,3]
b=["mango", "banana","apple"]
c=dict(zip(a,b))
print(dict(zip(a,b)))
