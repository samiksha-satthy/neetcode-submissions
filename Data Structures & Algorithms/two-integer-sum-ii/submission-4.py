class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #2 pointers --> 1 at the start and 1 at the end 
        #condition: if p1 + p2 > target, move p2 and vice versa
        #return index + 1

        p1 = 0
        p2 = len(numbers) - 1

        while p1 < p2:
            total = numbers[p1] + numbers[p2]
            if total > target:
                p2 -= 1; 
            elif total < target:
                p1 += 1;
            else:
                return [p1+1, p2+1]
        

        