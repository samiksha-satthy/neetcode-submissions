class Solution:
    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1
        result = float('inf')

        mid = low + (high - low) // 2

        if nums[low] <= nums[mid]:
            result = min(nums[low], result)
            low = mid + 1

        else:
            result = min(nums[mid], result)
            high = mid - 1

        while low <= high:
            result = min(nums[low], result)
            low += 1

        return result

            
        