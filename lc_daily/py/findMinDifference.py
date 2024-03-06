from datetime import datetime


class Solution:
    def findMinDifference(self, timePoints):
        time_list = []
        for time in timePoints:
            time_obj = datetime.strptime(time, "%H:%M")
            time_list.append(time_obj)
        
        time_list.sort()
        
        min_diff = float('inf')
        for i in range(len(time_list)):
            diff = (time_list[(i+1) % len(time_list)] - time_list[i]).total_seconds() / 60
            min_diff = min(min_diff, diff)
        
        return min_diff


sln = Solution()
print(sln.findMinDifference(["23:59", "00:00"]))
