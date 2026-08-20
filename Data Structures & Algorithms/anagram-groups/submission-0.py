class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        #1. hashmap/arrays problem 
        #2. 
        
        h = {}

        for str in strs:
            sorted_str = sorted(str)
            key = tuple(sorted_str)

            if key in h:
                h[key].append(str)
            else:
                h[key] = [str]
        
        return list(h.values())

        