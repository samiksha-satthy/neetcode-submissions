class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #sort the array
        #put elements in hash map (num : index)
        #loop through list looking at hash for a few conditions:
            #if first element in the sequence 
                #then add to result array and clear existing array 

        h = set(nums)
        
        finalCount = 0 
        for num in nums:
            if num - 1 not in h:
                count = 0
                while num + count in h:
                    
                     count += 1
                finalCount = max(count, finalCount)

        return finalCount

        

        