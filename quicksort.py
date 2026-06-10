#quicksort
def quicksort(arr,low,high):
    if low<high:
        ind=partition(arr,low,high)
        quicksort(arr,low,ind-1)
        #if ind+1<high:
        quicksort(arr,ind+1,high)
    
def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while(i<j):
        while(i<high and arr[i+1]<=pivot):
            i+=1
        while(arr[j-1]>pivot and j>low):
            j-=1
        if (i<j):
            #swap
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
arr=[5,6,6,1,2,4,1,2,6,5,9]
quicksort(arr,0,10)
