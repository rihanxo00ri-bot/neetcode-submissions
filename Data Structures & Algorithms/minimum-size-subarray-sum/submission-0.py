class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        mins=float('inf')
        sums=0
        i=0
        while i<= len(nums)-1:
            sums+=nums[i]
            while sums>=target:
                mins=min(mins,i-l+1)
                sums-=nums[l]
                l+=1
           
            i+=1        
        return mins if mins!= float('inf') else 0      