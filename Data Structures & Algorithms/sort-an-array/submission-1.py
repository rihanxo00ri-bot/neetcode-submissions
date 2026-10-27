class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        arr=nums
        if not arr:
            return []

        k=max(arr)
        K_min=min(arr)
        range_size=k - K_min +1
        count_arr=[0]*range_size
        for i in arr:
            count_arr[i-K_min]+=1
        sort_arr=[]
        index=0
        for j in range(len(count_arr)):
            for _ in range(count_arr[j]):
                sort_arr.append(j+K_min)
        return sort_arr
