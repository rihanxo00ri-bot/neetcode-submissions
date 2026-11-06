class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p= sorted(people)
        l=0
        r=len(p)-1
        boat_count=0
        while l<=r:
            if p[l]+p[r]<=limit:
                l+=1
                r-=1
            else:
                r-=1
            boat_count+=1         
            
        return boat_count                