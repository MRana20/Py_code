# solution using memoization
def maximumPoints(self, mat):
    # code here
    n = len(mat)
    cred = [ [0]*3 for i in range(n)]
    def f(day, act1):
        if cred[day][act1] != 0 :
            return cred[day][act1]
        if day == n-1 :
            cred[day][act1]=mat[n-1][act1]
            return mat[n-1][act1]
        
        act2 = (act1 + 1)%3
        act3 = (act1 + 2)%3
        
        cred[day][act1] = mat[day][act1] + max( f(day + 1 , act2), f(day+1 , act3) )
        return cred[day][act1]
    
    maxcred = max( f(0,0) ,f(0,1) , f(0,2))
    return maxcred


# solution using tabulation 
"""def maximumPoints(self, mat):
    # code here
    n = len(mat)
    cred = [ [0]*3 for i in range(n)]
    
    cred[n-1][0] = mat[n-1][0]
    cred[n-1][1] = mat[n-1][1]
    cred[n-1][2] = mat[n-1][2]
    for day in range(n-2,-1,-1):
        for act1 in [0,1,2]:
            act2 = (act1 + 1)%3
            act3 = (act1 + 2)%3
            cred[day][act1] = mat[day][act1] + max( cred[day + 1][act2] , cred[day+1][act3] )
            
        
    maxcred = max( cred[0][0], cred[0][1], cred[0][2])"""
    return maxcred
