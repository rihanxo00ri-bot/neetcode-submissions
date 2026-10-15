class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i+1, len(nums)):
                if temp == nums[j]:
                    print("true")
                    return
            print("false")   
