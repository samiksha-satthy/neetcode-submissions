class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #sort array 
        #iterate with index i, and p1=i+1 and p2=n-1
        #use -nums[i] as the target 

        sort = sorted(nums)

        result = []

        for i in range(len(sort) - 1):
            if i > 0 and sort[i - 1] == sort[i]:
                continue

            p1 = i + 1
            p2 = len(sort) - 1

            while p1 < p2:
                sum = sort[p1] + sort[p2]

                if sum > -sort[i]:
                    p2 -= 1

                elif sum < -sort[i]:
                    p1 += 1

                else:
                    result.append([sort[i],sort[p1], sort[p2]])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and sort[p1] == sort[p1 - 1]:
                        p1 += 1
                    while p1 < p2 and sort[p2] == sort[p2 + 1]:
                        p2 -= 1
        return result



        