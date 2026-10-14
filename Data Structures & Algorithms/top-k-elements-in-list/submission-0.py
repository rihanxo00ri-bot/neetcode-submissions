import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts ={}
        for i in nums:
            if i not in dicts:
                dicts[i]=1    
            dicts[i]= dicts[i]+1 

        top_k = heapq.nlargest(
            k,
            dicts.items(),
            key= lambda item: item[1]
        )  

        return[j[0] for j in top_k]

