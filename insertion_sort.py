#insertion sort
arr=[14,9,15,12,6,8,13]
n=len(arr)
for i in range(1,n):
    key=arr[i]
    while key<arr[i-1] and i-1>=0:
        #shift
        arr[i]=arr[i-1]
        i-=1
        arr[i]=key
    print(arr)
print(arr)
        
