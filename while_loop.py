a=[1,2,3,4,5]
result=0

i=0
n=len(a)
while i<n:
    result=result+a[i]
    i+=1
print(result)

b=[-10,2,19,-3,-5]
i=0
while i<len(b):
    if b[i]<0:
        b[i]=0
    i+=1
    print(b)
         