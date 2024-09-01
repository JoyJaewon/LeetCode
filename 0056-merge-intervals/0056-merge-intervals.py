class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        ans.append(intervals[0])

        for interval in intervals[1:]:
            start, end = interval
            if start <= ans[-1][1]:
                ans[-1] = [min(ans[-1][0], start), max(ans[-1][1], end)]
            else:
                ans.append(interval)
        
        return ans
        