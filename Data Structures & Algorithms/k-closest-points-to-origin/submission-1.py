import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        result = []

        for point in points:
            distance = (point[0] ** 2) + (point[1] ** 2)
            minHeap.append([distance, point])

        heapq.heapify(minHeap)


        while k > 0:
            points = heapq.heappop(minHeap)[1]

            result.append(points)
            k -= 1

        return result