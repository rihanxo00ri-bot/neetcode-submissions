class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        H=max(piles)
       
        while l<=H:
            mid=(l+H)//2
            hours=0
            for pile in piles:
                hours+=(pile+mid-1)//mid
                
            if hours<=h:
                H=mid-1
            else:
                l=mid+1
        return l            
        