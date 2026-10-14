class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #first find the frequency of each word
        dic ={}
        for word in strs:
          sort_s =   "".join(sorted(word))
          if sort_s in dic:
            dic[sort_s].append(word)
          else:
              
            dic[sort_s] = [word] 
        return list(dic.values())