#merge sort
def merge_sort(arr,low,high):
    if low==high:
        return
    mid=(low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)
def merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while(left<=mid and right<=high):
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    if left>mid and right<=high:
        temp.extend(arr[right:])
    if right>high and left<=mid:
        temp.extend(arr[left:mid+1])
    for i in range(low,high+1):
        arr[i]=temp[i-low]
arr=[3,1,2,4,5,3,1]
merge_sort(arr,0,6)
