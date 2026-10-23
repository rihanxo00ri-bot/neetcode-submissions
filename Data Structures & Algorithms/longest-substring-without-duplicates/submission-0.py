class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset =set()
        left=0
        freq=0
        for i in range(len(s)):
           while s[i] in hashset:
            hashset.remove(s[left])
            left+=1 
           hashset.add(s[i])
           freq = max(freq, i - left + 1)


        return freq           

            