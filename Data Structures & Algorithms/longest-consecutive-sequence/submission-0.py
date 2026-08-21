class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #sort the array
        #put elements in hash map (num : index)
        #loop through list looking at hash for a few conditions:
            #if first element in the sequence 
                #then add to result array and clear existing array 

        h = set()

        for num in nums:
            h.add(num)
        
        finalCount = 0 
        for num in nums:
            if num - 1 not in h:
                track = True 
                count = 0
                i = 0
                while track:
                    if num + i not in h:
                        track = False 
                        if count > finalCount:
                            finalCount = count 
                        break
                    else:
                        count += 1
                        i += 1

        return finalCount

        

        