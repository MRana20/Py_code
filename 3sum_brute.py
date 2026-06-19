class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        out=[]
        ith=jth=kth=-10**6
        if n<=2:
            return []
        for i in range(n-2):
            if nums[i]==ith:
                continue
            check=nums[i]
            need=0-check
            
            for j in range(i+1,n-1):
                if nums[j]==jth:
                    continue
                for k in range(j+1,n):
                    if nums[k]==kth:
                        continue
                    if nums[j]+nums[k]==need:
                        out.append([nums[i],nums[j],nums[k]])
                    kth=nums[k]
                jth=nums[j]
                kth=-10**6
            ith=nums[i]
            jth=-10**6
        return out
            
