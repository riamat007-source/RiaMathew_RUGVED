def caeserscipher(s,sh):
    s=s.lower()
    y=""
    A=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in s:
        if i in A:
            if (A.index(i)+sh)<26:
                y+=A[A.index(i)+sh]
            else:
                y+=A[A.index(i)+sh-26]
        else:
            y+=i
    print(y)
s=input("enter string")
sh=int(input("Enter shift key"))
caeserscipher(s,sh)

    
