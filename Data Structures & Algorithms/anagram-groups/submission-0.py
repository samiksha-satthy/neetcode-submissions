class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        #1. hashmap/arrays problem 
        #2. 
        
        actual = {}

        for str in strs:
            count = [0]*26
            for s in str:
                index = ord(s) - ord('a')
                count[index] += 1
            key = tuple(count)

            if key not in actual:
                actual[key] = []

            actual[key].append(str)

        return list(actual.values())


                
        


        