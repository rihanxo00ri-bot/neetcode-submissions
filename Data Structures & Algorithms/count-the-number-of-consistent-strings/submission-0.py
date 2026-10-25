class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hashset =set(allowed)
        count=0
        for word in words:
            is_consit=True
            for char in word:
                if char not in hashset:
                    is_consit=False
                    break
            if is_consit:
                count+=1        
                
            
        return count            
        
        