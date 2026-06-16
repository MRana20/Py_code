def leaders(arr):
        outlist=[]
        for i in range(len(arr)-1):
            flag=0
            for j in range(i+1,len(arr)):
                if arr[j]>arr[i]:
                    flag=1
                    break
            if flag==0:
                outlist.append(arr[i])
            
        outlist.append(arr[-1])
        return outlist
