class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        
        need = {}
        window = {}  # Fixed typo here (+ to =)

        for c in t:
            need[c] = need.get(c, 0) + 1    

        left = right = 0
        start = 0
        valid = 0
        lenght = float('inf')

        while right < len(s):
            char = s[right]
            right += 1
            
            # If the character is part of what we need, track it in our window
            if char in need:
                window[char] = window.get(char, 0) + 1
                if window[char] == need[char]:
                    valid += 1
            
            # When we have all required characters, shrink from the left
            while valid == len(need):
                if right - left < lenght:
                    start = left
                    lenght = right - left
                
                d = s[left]
                left += 1
                
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                    
        return "" if lenght == float('inf') else s[start:start + lenght]