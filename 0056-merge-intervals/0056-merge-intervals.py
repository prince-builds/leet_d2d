class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result=[]
        cur=intervals[0]

        for interval in intervals[1:]:
            if interval[0]<=cur[1]:
                cur[1]=max(interval[1],cur[1])
            else:
                result.append(cur)
                cur=interval
        result.append(cur)
        return result
        