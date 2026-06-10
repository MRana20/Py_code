#selection sort
arr=[8,28,13,17,18,49,17,16,29]
copy=arr
#8 13 16 17 18 49 17 28 29
for i in range(len(arr)-1):
    slice_arr=arr[i:]
    print(slice_arr)
    ind=slice_arr.index(min(slice_arr))+i
    
    arr[i],arr[ind]=arr[ind],arr[i]
    print(arr)
    print(" ")

print(arr)
