class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            temp = num[i]
            for j in nums:
                if temp == nums[j]:
                    print("true")
                    return
                print("false")   
