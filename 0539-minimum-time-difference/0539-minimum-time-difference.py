'''
input: list[str] - list of times in hh:mm format
output: integer minimum minutes difference 

Clarifications
- do we just look at the minute, or hour as well? 20:00, 22:00 => 120?


Test Cases
[23:59, 00:00] -> 0
[00:00, 00:00] -> 0
[20:00, 22:00] -> 120
[08:10, 09:20, 12:11, 21:00, 23:00, 23:59] -> 59 

Approach 1) compare each combinations and track minimum. O(N^2)
Approach 2) sort. one pass


'''
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [False] * 1440  # 24 * 60 = 1440 mins

        for time in timePoints:
            hr, minute = time.split(':')
            total_minutes = int(hr) * 60 + int(minute)

            # duplicated time found
            if minutes[total_minutes]:
                return 0
            minutes[total_minutes] = True

        first_time = float('inf')
        last_time = float('-inf')
        prev_time = float('-inf')
        min_diff = float('inf')

        for i in range(1440):
            if minutes[i]:
                if first_time == float('inf'):
                    first_time = i
                if prev_time != float('-inf'):
                    min_diff = min(min_diff, i - prev_time)
                prev_time = i
                last_time = i

        min_diff = min(min_diff, 1440 - last_time + first_time)

        return min_diff
