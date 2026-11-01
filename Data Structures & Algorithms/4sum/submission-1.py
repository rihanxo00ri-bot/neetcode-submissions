class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j >i+1 and nums[j]==nums[j-1]:
                    continue
                
                p =j+1
                q=len(nums)-1
                while p<q:
                    sums = nums[i] +nums[j]+nums[p]+nums[q]
                    if sums == target:
                        res.append([nums[i] ,nums[j],nums[p],nums[q]])
                        p+=1
                        q-=1
                        while p < q and nums[p] == nums[p - 1]:
                            p += 1
                        while p < q and nums[q] == nums[q + 1]:
                            q -= 1
                    elif sums>target:
                        q-=1
                    else:
                        p+=1            

        return res                
        