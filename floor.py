def findFloor(self, arr, x):
    # code here
    low=0
    m=len(arr)
    high=m-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>x: # i just don't want anything to do with this
            #left half
            high=mid-1
        if arr[mid]<x:
            if mid==low:
                if arr[high]<=x:
                    return high
                else:
                    return mid
            else:
                low=mid

        if arr[mid]==x:
            if mid==m-1: #will check first thing first and if true the entire or becomes true
                return mid
            if arr[mid+1]!=x:
                return mid
            else:
                if mid==low:
                    if arr[high]<=x:
                        return high
                    else:
                        return mid
                else:
                    low=mid # there is a chance this keeps running
        if low==high and not arr[low]<=x:
            return -1
        
        
    return -1
