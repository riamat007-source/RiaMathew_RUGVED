def val(x):
    sum=0
    for i in x[0::2]:
        if int(i)*2<10:
            sum+=int(i)*2
        else:
            y=int(i)*2
            while y>0:
                sum+=y%10
                y=y//10
    for i in x[1::2]:
        sum+=int(i)
    if sum%10==0:
        print("credit card number is valid")
    else:
        print("credit card number is invalid")
x=input("enter credit card number")
val(x)
