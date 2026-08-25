class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #2 pointers -> starting at beginning to end 
        #condition:
            #move 2nd pointer all the way to end 
            #then start moving 1st pointer 

        area = 0
        p1 = 0
        p2 = len(heights) - 1

        while p1 < p2:
            current = min(heights[p1], heights[p2]) * (p2 - p1)
            area = max(area, current)
            if heights[p2] < heights[p1]:
                p2 -= 1
            else:
                p1 += 1

        return area
        