def maxProfit(self, prices):
        minimum=prices[0]
        maxprof=0
        for i in range(1,len(prices)):
            if prices[i]<minimum:
                minimum=prices[i]
            else:
                profit=prices[i]-minimum
                maxprof=max(maxprof,profit)
        return maxprof
