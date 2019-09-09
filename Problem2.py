import heapq

class Solution:
	def MeetingRooms(self, intervals):
		queue = []
		if len(intervals) == 0:
			return 0
		intervals = sorted(intervals, key=lambda x:x[0])
		heapq.heappush(queue, intervals[0][1])
		for i in intervals[1:]:
			if i[0] > queue[0]:
				heapq.heappop(queue)
				heapq.heappush(queue, i[1])
			else:
				heapq.heappush(queue, i[1])
		return len(queue)

if __name__ == '__main__':
	mr = Solution()
	print(mr.MeetingRooms([[0,30],[5,32],[15,20],[6,16]]))