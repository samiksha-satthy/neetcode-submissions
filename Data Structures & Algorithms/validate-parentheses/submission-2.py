class Solution:
    def isValid(self, s: str) -> bool:

        #define which bracket should go to which one 
        #keep track of all elements in the stack
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

 
        #check if that elemnt is a closing bracket 
            #if it is closing, then pop last element in stack to compare
                #if they map, then continue 
                #otherwise return false 

        #if it is not a closing bracket, then add to stack 
        for st in s:
            if st in mapping and stack:
                last = stack.pop()
                if mapping[st] != last:
                    return False 
            else:
                stack.append(st)

        return not stack

        