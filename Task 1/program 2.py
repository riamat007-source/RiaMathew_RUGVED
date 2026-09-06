y=input("Enter string")
dict={}
x=list(y)
for i in range(len(x)-1):
    min=i
    for j in range(i+1,len(x)):
        if x[min]>x[j]:
            min=j
    t=x[i]
    x[i]=x[min]
    x[min]=t
y=""
for i in x:
    y+=i
print(y)
x=list(y)
for i in range(len(x)):
    if x[i] in dict:
        continue
    else:
        dict[x[i]]=x.count(x[i])
for i in dict.items():
    print(i)
