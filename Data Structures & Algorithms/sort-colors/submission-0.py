class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=len(nums)-1
        num=0
        while num<=right:
           if nums[num]==0:
            nums[num],nums[left]=nums[left], nums[num]
            left+=1
            num+=1
           elif nums[num]==2:
            nums[num],nums[right]=nums[right],nums[num] 
            right-=1
           else:
            num+=1 
        return nums    
