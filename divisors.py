#all divisors
import math
n=int(input("Enter an integer : "))
d=[]
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        d.append(i)
        d.append(int(n/i))
print(d)
if len(d)==2:
    print("isprime")
