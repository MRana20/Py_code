def maxSubArray(self, nums):
        max_sum=float("-inf")
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            max_sum=max(max_sum,sum)
            if sum<0:
                sum=0
        return max_sum
        
# if you want the array, use starting point as when the sum==0, and put the conditional for sum> max and within it add actual start and actual end and
# update as needed
