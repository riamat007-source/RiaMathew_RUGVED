arr=eval(input("enter an array in the form [x,y,]"))
for i in arr:
    if arr.count(i)>1:
        print("the first recurring element is",i)
        print("Index:",arr.index(i))
        break
    
