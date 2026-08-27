class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        result = set()
        l = 0
        maxCount = 0

        for r in range(len(s)):

            while s[r] in result:
                result.remove(s[l])
                l += 1

            result.add(s[r])
            maxCount = max(maxCount, len(result))

        return maxCount


        