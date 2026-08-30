class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        h = {}

        for s in s1:
            if s in h:
                h[s] += 1
            else:
                h[s] = 1
        
        l = 0
        
        temp = {}
        for r in range(len(s2)):

            l = max(0, r - len(s1) + 1)

            if s2[r] in temp:
                temp[s2[r]] += 1
            elif s2[r] not in temp:
                temp[s2[r]] = 1 

            if r - l + 1 == len(s1):
                if h == temp:
                    return True 
                temp[s2[l]] -= 1
                if temp[s2[l]] == 0:
                    temp.pop(s2[l], None)
                    

        return False



        