class Solution:
    def isPalindrome(self, s: str) -> bool:

        result = "".join(char.lower() for char in s if char.isalnum())

        s1 = 0
        s2 = len(result) - 1

        while s1 < s2:
            if result[s1] != result[s2]:
                return False
            s1+=1
            s2-=1
        return True
        