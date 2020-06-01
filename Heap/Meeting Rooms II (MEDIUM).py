"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
https://leetcode.com/problems/meeting-rooms-ii/solution/
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        ##[0, 30],[5, 10],[9, 13],[15, 20]
        
        [0, 30], [35, 40]
        heap = [10,30]
        
        1. Add the ending time to the min-heap
        2. Loop over all of the intervals
            a. Look at the starting time --- if the starting time of curr interval is >= heap[0]:
                - heappop
            b. Add the curr interval end time to the heap
        3. Return heap size
        """
        
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[0])
        heap = []
        
        # Appending the ending time of the first element of intervals
        heap.append(intervals[0][1])
        
        for startTime, endTime in intervals[1:]:
            
            if startTime >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, endTime)
            
        return len(heap)

# O(nlogn) time and O(1) space
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        startTimes = [x[0] for x in intervals]
        endTimes = [x[1] for x in intervals]
        
        startTimes.sort()
        endTimes.sort()
        
        s_ptr, e_ptr = 0, 0
        
        rooms = 0
        while s_ptr < len(startTimes):
            if startTimes[s_ptr] >= endTimes[e_ptr]:
                rooms -= 1
                e_ptr += 1
            rooms += 1
            s_ptr += 1
        return  rooms