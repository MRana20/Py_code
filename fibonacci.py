#fibonacci
n=10
l=[0,1]
i=0
while (i<n-2):
    l.append(l[-1]+l[-2])
    i=i+1
print(l[-1]) #0 1 1 2 3 5 8 13 21 34

#better
secondlast=0
last=1
for i in range(n-2):
    current = secondlast+last
    secondlast=last
    last=current
print(current)
    
    
