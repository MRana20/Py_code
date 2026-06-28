def aggressiveCows(stalls, k):
    stalls.sort() # o(logn)
    n=len(stalls)
    maxi=stalls[-1]
    mini=stalls[0]

    low=1
    high=maxi-mini
    ans=-1
    while(high>=low):
        mid_dist=(low+high)//2
        if possible(stalls,mid_dist,k,n):
            ans=max(ans,mid_dist)
            low=mid_dist+1
        else:
            high=mid_dist-1
    return ans
    pass
def possible(stalls,mid_dist,k,n): # k is the number of cows
    k-=1 # already placed at the first position
    position = 0
    for i in range(1,n):
        if stalls[i]-stalls[position]>=mid_dist and k>0:
            k-=1
            position=i
    '''while i < n-1 and k!=0:
        j=i+1
        while j<n and k!=0 :
            if stalls[j]-stalls[i]>=mid_dist:
                k-=1
                break
            j+=1
        i=j'''
    if k==0: return True
    return False
