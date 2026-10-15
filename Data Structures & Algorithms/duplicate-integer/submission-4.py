class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            temp = i
            for j in range(len(nums)):
                if temp == j+1:
                    print("true")
                    return
            print("false")   
