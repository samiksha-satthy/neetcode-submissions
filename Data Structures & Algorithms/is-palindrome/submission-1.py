class Solution:
    def isPalindrome(self, s: str) -> bool:


        s1 = 0
        s2 = len(s) - 1

        while s1 < s2:
            if not s[s1].isalnum():
                s1+=1
                continue
            if not s[s2].isalnum():
                s2-=1
                continue
            if s[s1].lower() != s[s2].lower():
                return False
            s1+=1
            s2-=1
            
        return True
        