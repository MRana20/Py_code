#sum
def sumnum(n):
    if (n==1):
        return 1
    sum=sumnum(n-1)+n
    return sum
print(sumnum(5))
