#number of digits
import math
n=int(input("Enter an integer : "))
'''dig=0
while(n>0):
    n=n//10 #which is better? n//10 or n/10--- n//10 because it goes to 0 when all digs counted, so while loop terminates
    dig+=1
    #print(dig)
print(dig)'''
dig=math.floor(math.log10(n))+1
print(dig)
