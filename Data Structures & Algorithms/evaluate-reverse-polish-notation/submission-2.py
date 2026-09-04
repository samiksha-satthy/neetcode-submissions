class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        #check if token is operator with a bunch of if statements 
            #if it is, then pop the last 2 elements and perform operation, save back into stack  
        #if not operation, save number into stack 
        for token in tokens:

            match token:
                case "+":
                    first = int(stack.pop())
                    second = int(stack.pop())
                    res = first + second 
                    stack.append(res)
                case "-":
                    first = int(stack.pop())
                    second = int(stack.pop())
                    res = second - first 
                    stack.append(res)

                case "*":
                    first = int(stack.pop())
                    second = int(stack.pop())
                    res = first * second 
                    stack.append(res)

                case "/":
                    first = int(stack.pop())
                    second = int(stack.pop())
                    res = second / first
                    stack.append(res)
                
                case _:
                    stack.append(token)




        #return result 
        return int(stack[-1])

        