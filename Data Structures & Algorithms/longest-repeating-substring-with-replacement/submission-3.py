class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        result = defaultdict(int)
        maxCount = 0
        maxFreq = 0
        l = 0
        

        for r in range (len(s)):

            result[s[r]] += 1
            maxFreq = max(maxFreq, result[s[r]])

            if r - l + 1 - maxFreq > k:
                result[s[l]] -= 1
                if result[s[l]] == 0:
                    del result[s[l]]
                l += 1

            maxCount = max(maxCount, r - l + 1)
        
        return maxCount

            


        
            
        