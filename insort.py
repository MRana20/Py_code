#insertion sort
l=list("INSERTIONSORT")
n=len(l)
for i in range(n):
    j=i
    while (j>0):
        if l[j]<l[j-1]:
            l[j],l[j-1]=l[j-1],l[j]
        j=j-1
print(l)
