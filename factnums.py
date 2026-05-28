#factorial numbers
n=int(input("Enter a number : "))
l=[]
fact=1
i=1
while(fact<=n):
    l.append(fact)
    fact=fact*(i+1)
    i=i+1
print(l)
#recursionnnn
'''if n==1:
    	    return [1]
        result=self.factorialNumbers(n-1) #goes to 1 and then returns [1]
        next_factorial_number=(1+len(result))*result[-1]
        if next_factorial_number<=n:
            result.append(next_factorial_number)
        return result'''
