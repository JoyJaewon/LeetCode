class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end_times = []

        for interval in intervals:
            start, end = interval

            if end_times and start >= end_times[0]:
                end_times.pop(0)
            
            end_times.append(end)
            end_times.sort()
        
        return len(end_times)