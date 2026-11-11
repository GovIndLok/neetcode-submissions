from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points.sort(key= lambda cordinate: sqrt(cordinate[0]**2 + cordinate[1]**2))

        return points[:k]