# some sort that i thought was insertion
arr=[14,9,15,12,6,8,13]
n=len(arr)
for i in range(1,n):
    while arr[i]<arr[i-1] and i-1>=0:
        #swap
        arr[i],arr[i-1]=arr[i-1],arr[i]
        i-=1
print(arr)
        
