text=input("enter text")
sentences=text.count(".")+text.count("!")+text.count("?")
l1=text.split()
words=len(l1)
letters=0
for i in l1:
    for ch in i:
        if ch.isalpha():
            letters+=1
L=(letters/words)*100
S=(sentences/words)*100
index=0.0588*L-0.296*S-15.8
print("The index of the given text is",index)
