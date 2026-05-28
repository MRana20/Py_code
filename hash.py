#hashing background
arr=[1,2,3,4,5,1,2,3,4]
query=[1,2,3,4,5]
d={}
for i in query: #for every element in the query, we count its freq in the arr
    #and then we put that as the value in a key value pair
    count=0
    for j in arr:
        if i==j:
            count+=1
    d[i]=count
print(d)
