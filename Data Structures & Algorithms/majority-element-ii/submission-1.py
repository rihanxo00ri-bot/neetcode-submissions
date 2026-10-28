class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candiate1,candiate2=None,None
        count_1=0
        count_2=0
        for num in nums:
            if count_1==0:
                candiate1=num
                count_1=1
            elif candiate1==num:
                count_1+=1
            elif count_2==0:
                candiate2=num
                count_2=1
            elif candiate2==num:
                count_2+=1
            else:
                count_1-=1
                count_2-=1   

        result=[]  
       
        for cand in (candiate1,candiate2):
            if cand is not None and nums.count(cand)>len(nums)//3:
                if cand not in result:
                    result.append(cand)

        return result 