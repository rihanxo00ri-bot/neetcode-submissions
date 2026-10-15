class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            temp = i
            for j in nums:
                if temp == j:
                    print("true")
                    return
            print("false")   
