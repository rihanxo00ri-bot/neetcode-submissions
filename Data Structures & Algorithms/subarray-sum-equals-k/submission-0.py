class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        count=0
        sum_k=0
        dif=0
        for num in range(len(nums)):
            sum_k+=nums[num]
            dif = sum_k -k
            if dif in hashmap:
                count+=hashmap[dif]
            
            hashmap[sum_k]=hashmap.get(sum_k,0)+1
        return count            