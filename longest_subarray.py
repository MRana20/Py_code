def longestSubarrayWithSumK(a,k)
    max_len=0
    n=len(a)
    for i in range(n-1):
        for j in range(i+1,n+1):
            subarray=a[i:j]
            if sum(subarray)==k:
                max_len=max(max_len,len(subarray))
    return max_len

