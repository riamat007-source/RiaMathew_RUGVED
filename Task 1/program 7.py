def fib(n):
    x=0
    y=1
    for i in range(n):
        print(x, end="\t")
        temp=x
        x=y
        y=temp+y
n=int(input("Enter a number"))
fib(n)

        
