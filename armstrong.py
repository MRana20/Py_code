#armstrong
import math
n=int(input("Enter a number: "))
dup=n
sum=0
numlen=len(str(n))
while(n>0):
    sum+=(n%10)**3
    n=n//10
print(sum==dup)
