d={}
arr=[3, 1, 4, 4, 5, 2, 6, 1]
k=5

#{1:2,2:1,3:1,4:2,5:1,6:1}

# 1 4 2 3 5 6
for i in arr:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
print(d)

new_d={}
for key, value in d.items():
    if value in new_d.keys():
        new_d[value].append(key)
    else:
        new_d[value]=[]
        new_d[value].append(key)

#sorted_d=dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

sorted_new_d=dict(sorted(new_d.items(),reverse=True))
##keylist=list(sorted_new_d.keys())
##
##lk=len(keylist)  #length of the key list
l=[]
for value in list(sorted_new_d.values()):
    l.extend(sorted(value,reverse=True))
print(l[0:k])
        
