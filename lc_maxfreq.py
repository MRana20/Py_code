#max_freq
nums=[1,4,7,8,13]


k=5
length=len(nums)
nums.sort()
freq_list=[]

for i in range(-1, -length-1,-1):
    freq=1  #so basically we are saying: for this number, we count freq.
    knew=k
    for j in range(i-1, -(length+1),-1):
        diff=nums[i]-nums[j]
        if diff>knew:
            break
        else:
            #we mentally increment nums[j] to nums[i] and now work with the remainder k
            freq+=1
            #update k
            knew-=diff
        freq_list.append(freq)


    
if freq_list != []:
    print(max(freq_list))
else:
        print(1)
