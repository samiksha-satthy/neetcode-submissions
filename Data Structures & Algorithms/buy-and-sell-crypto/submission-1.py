class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #start window at index=0 and 0+1 check that it doesnt exceed length 
        #if i2 < i1 then i1=i2; otherwise increase length of subarray 
        #check if any indexes are stored in results array 

        l = 0
        r = 1
        maxP = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
               maxP = max(maxP, prices[r] - prices[l]) 

            r += 1

        return maxP
        
        