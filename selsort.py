# selection sort
string="SELECTIONSORT"
s=list(string)
n=len(s)
for i in range(0,n):
    min=i
    for j in range(i+1,n) :
        if (s[min]>s[j]):
            min=j
    s[i],s[min]=s[min],s[i]

print(s)
