n=int(input("enter n:"))
m=[]
r=[]
for i in range(n):
    row=eval(input("enter row as a list"))
    m.append(row)
for i in range(n):
    row=[]
    for j in range(n-1,-1,-1):
        row.append(m[j][i])
    r.append(row)
print("rotated matrix")
for k in r:
    print(k)
print("spiral order")
top=0
bottom=n-1
left=0
right=n-1
while top<=bottom and left<=right:
    for j in range(left, right + 1):
        print(r[top][j], end=" ")
    top+=1
    for i in range(top, bottom + 1):
        print(r[i][right], end=" ")
    right -= 1
    if top <= bottom:
        for j in range(right, left - 1, -1):
            print(r[bottom][j], end=" ")
        bottom -= 1
    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(r[i][left], end=" ")
        left += 1
