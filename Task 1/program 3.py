x=int(input("enter number"))
y=str(x)
h=0
for i in range(len(y)):
    if i==len(y)-1:
        if int((y[i]))<int(y[i-1]) and h!=3:
            h=2
    elif int(y[i])<int(y[i+1]) and h!=2:
        h=1
    elif int(y[i])>int(y[i+1]):
        h=2
    else:
        h=3
if h==2:
    print("Hill Number")
else:
    print("not a hill number")
    
    
