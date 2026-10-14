class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i+1,len(nums)):
                sum = temp+nums[j]
                if sum == target:
                    index = [i,j]
                    return index