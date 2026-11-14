class TimeMap:

    def __init__(self):
        self.HashTable = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.HashTable:
            self.HashTable[key] = []
        
        self.HashTable[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        ans = ""
        values = self.HashTable.get(key, [])

        left = 0
        right = len(values) - 1
        while left <= right:
            
            mid = (left + right) // 2
            if values[mid][1]  <= timestamp:
                ans = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return ans