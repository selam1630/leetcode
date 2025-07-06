class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map={}
        maxle=0
        start=0
        for i in range (len(s)):
            if s[i] in char_map and char_map[s[i]]>=start:
                start=char_map[s[i]]+1
            char_map [s[i]]=i
            maxle=max(maxle,i-start+1)
        return maxle
            
            