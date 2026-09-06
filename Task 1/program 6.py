x=input("enter a string")
y=input("enter second string")
rep=0
l=list(y)

for i in x:
    if i in l:
        l.remove(i)
    else:
        print(x,"and",y,"are not anagrams")
        rep=1
        break
if rep==0:
    print(x,"and",y,"are anagrams")
    

    
            
        
