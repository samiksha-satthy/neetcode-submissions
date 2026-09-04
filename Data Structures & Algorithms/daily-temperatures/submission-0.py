class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0] * len(temperatures)

        #if stack is not empty, check the current temp with first element 
            #if current temp is higher than the pre temp, pop it out 
            #calculate the index difference (i-0)
        #if stack is empty, just add the num 
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                    wait = stack.pop()
                    res[wait] = i - wait
            stack.append(i)

        return res



        