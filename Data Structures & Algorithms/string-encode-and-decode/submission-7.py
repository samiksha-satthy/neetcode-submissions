class Solution:

    #store as a string (space between items)
    #iterate through the list
    # store the current item as a result string
    #check if it's the last element in the list 
        #used to determine if we need a space 
    def encode(self, strs: List[str]) -> str:

        result = str()

        for i, string in enumerate(strs):
            result += str(len(string))
            result += '#'
            result += string
        return result


    #iterate through the string
    #when there's a space (not alpha), store that as a separate term 
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while (s[j] != '#'):
                j += 1

            num = int(s[i:j])
            word = s[j+1:j+num+1]
            result.append(word)
            i = j+num+1
        return result
            



        
