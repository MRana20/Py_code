def majorityElement(self, arr):
    #code here
    i=1
    ctr=1
    count=0
    ele=arr[0]
    while (i<len(arr)):
        if ctr==0:
            ele=arr[i]
            ctr=1
        else:
            if arr[i]==ele:
                ctr+=1
            else:
                ctr-=1
        i+=1
    for j in arr:
        if j==ele:
            count+=1
    if count>len(arr)//2:
        return ele
    else:
        return -1
