max_len=0
a=[1,2,3,1,2,3]
k=3
#prefix sum
n=len(a)
hasharr=[0]*n
hasharr[0]=a[0]
for i in range(1,n):
    hasharr[i]=hasharr[i-1]+a[i]
    if hasharr[i]==k:
        max_len=i+1

for i in range(n): #0 to n-1
    for j in range(i+1): #0 to i
        if hasharr[j]==hasharr[i]-k:
            length=i-j
            max_len=max(max_len,length)

