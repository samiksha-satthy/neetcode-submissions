class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = {}
        answer = list()

        for i, num in enumerate(nums):
            h[num] = i

        for i, num in enumerate(nums):
            expect = target - num 
            if expect in h and h[expect] != i:
                return [i, h[expect]]

        