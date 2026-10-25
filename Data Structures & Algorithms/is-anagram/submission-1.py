class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
       if len(s)!=len(t):
        return False
       arr_s=[0]*26
       arr_t=[0]*26
       for i in s:
        arr_s[ord(i)-ord('a')]+=1
       for j in t:
        arr_t[ord(j)-ord('a')]+=1
       return arr_s==arr_t
           