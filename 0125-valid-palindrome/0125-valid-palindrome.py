class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = ''.join(c.lower() for c in s if c.isalnum())
        right=0
        left=len(f)-1
        while right<left:
            if f[right]!=f[left]:
                return False
            left-=1
            right+=1
        return True
       
       
        
    
       
