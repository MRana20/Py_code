def rearrangeArray(self, nums):
        pos_list=[]
        neg_list=[]
        for i in nums:
            if i<0:
                neg_list.append(i)
            else:
                pos_list.append(i)
        newnums=[]
        for i in range(len(pos_list)):
            newnums.append(pos_list[i])
            newnums.append(neg_list[i])
        return newnums
