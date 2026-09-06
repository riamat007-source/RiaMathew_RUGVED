def str1(x,n):
    check=0
    l=[x[0:n],]
    if len(x)%n!=0:
        print("cannot be divided")
        return
    for i in range(int(len(x)/n-1)):
        if x[0:n]==x[n:n+n] and check==0:
            check=0
            l.append(x[n:n+n])
        else:
            check=1
    if check==0:
        print(l)
    else:
        print("sequence is not the same")
x=input("Enter String")
n=int(input("enter number for division"))
str1(x,n)


    
