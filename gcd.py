#gcd
n1=6
n2=12
##for i in range (min(n1,n2),0,-1):
##    if (n1%i==0 and n2%i==0):
##        gcd=i
##        break
##print(gcd)
#recursion

def gcd(n1,n2):
    while(n1>0):
        if (n1>n2):
            n1=n1-n2
            gcd=gcd(n1,n2)
        else:
            n2=n2-n1
            gcd=gcd(n1,n2)
            
    if(n1==0):
        return n2
n1=int(input("Enter number 1 : "))
n2= int(input("Enter number 2 : "))
gcd=gcd(n1,n2)
print(gcd)
