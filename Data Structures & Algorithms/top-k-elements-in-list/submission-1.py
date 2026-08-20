class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        h = {}

        for num in nums:
            h[num] = h.get(num, 0) + 1

        result = []
        for i in range(k):
            frequent = max(h, key=h.get)
            result.append(frequent)
            h.pop(max(h, key=h.get))
        
        return result

        