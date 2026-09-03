class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)
        lowest = high
        while low <= high:
            mid = low + (high - low) // 2
            
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            

            if hours <= h:
                lowest = mid
                high = mid - 1

            elif hours > h:
                low = mid + 1

        return lowest
                



            




            


