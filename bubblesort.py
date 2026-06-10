#bubble sort
arr=[13,46,24,52,20,9]
n=len(arr)
iter=0
for i in range(n-1):
    slice_list=arr[:n-i]
    m=len(slice_list)
    for j in range(m-1):
        if arr[j]<arr[j+1]:
            continue
        else:
            arr[j],arr[j+1]=arr[j+1],arr[j] #swapping
            print(arr)
            
print(arr)
