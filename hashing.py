#hash

#precompute:
string="abcabmcdefge"
q=int(input("Enter number of queries : "))
hash=[0]*26
for i in range(len(string)):
    index=ord(string[i])-ord('a')
    hash[index]+=1;
while (q>0):
    c=input("Enter a character : ")
    print(hash[ord(c[0])-ord('a')])
    q-=1
