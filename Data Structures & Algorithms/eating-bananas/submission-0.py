class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        lasthr = 0
        while left <= right:
            mid = (left + right) // 2
            hrs = 0
            

            for i in range(len(piles)):
                hrs += piles[i] // mid
                if piles[i] % mid != 0:
                    hrs += 1
                
            
            if hrs <= h:
                lasthr = mid
                right = mid - 1
            else:
                left = mid + 1

        return lasthr


