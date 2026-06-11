
"""
:type nums: List[int]
:rtype: None Do not return anything, modify nums in-place instead.
"""
nums=[1,0,2,3,2,0,0,4,5,1]
i=0
fin=len(nums)
while(i<fin):
    j=1+i
    if nums[i]==0:
        
        while(j<fin):
            nums[j-1]=nums[j] # shift the non-zero numbers to the left
            j+=1
        nums[j-1]=0
        fin-=1
        i-=1
    i+=1
