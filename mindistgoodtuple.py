import itertools
def funct(nums):   
   n=len(nums)
   if n<3:
       return -1
   #another case to return -1 is if size more than three but no good tuple
   hasharray=[0]*(max(nums)+1)
   final_dict={}
   for i in nums:
       hasharray[i]+=1
   for j in hasharray:
       if j>=3:
           actual_num=hasharray.index(j) #the actual number whose frequency is j, stored in ha
           #list_of_indices_for_selected_number
           l=[i for i, e in enumerate(nums) if e==actual_num]
           
           dist_dict={}
           for triplet in itertools.combinations(l,3):
               distance=abs(triplet[1]-triplet[0])
               +abs(triplet[2]-triplet[1])
               +abs(triplet[0]-triplet[2])
               
               dist_dict[triplet]=distance
           mindist=min(dist_dict.values())

           l1=list(dist_dict.values())
           l2=list(dist_dict.keys())
           besttuple=l2[l1.index(mindist)]
           final_dict[besttuple]=mindist
       
   l3=list(final_dict.values())
   l4=list(final_dict.keys())
   minfinal=min(final_dict.values())
   bestest=l4[l3.index(minfinal)]
   return minfinal

nums=[1,2,1,1,3]
print(funct(nums))




hasharray=[0]*(max(nums)+1)
       final_dict={}
       for i in nums:
           hasharray[i]+=1
       finald=[]
       for j in range(len(hasharray)):
           if hasharray[j]>=3:
               actual_num=j #the actual number whose frequency is j, stored in ha
               #list_of_indices_for_selected_number
               l=[i for i, e in enumerate(nums) if e==actual_num]
               
               
               d=[]
               for triplet in itertools.combinations(l,3):
                   distance=abs(triplet[1]-triplet[0])+abs(triplet[2]-triplet[1])+abs(triplet[0]-triplet[2])
                   d.append(distance)


               mindist=min(d)
               finald.append(mindist)

       if not finald:
           return -1
       else: 
           return min(finald)

