class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        h = {}

        if len(s) != len(t):
            return False

        for s1 in s:
            h[s1] = h.get(s1, 0) + 1
        
        for t1 in t:
            if t1 in h and h[t1] > 0:
                h[t1] -= 1
            else:
                return False
        return True
        