class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for string in strs:
            charts = [0] * 26
            for char in string:
                char_num = ord(char) - ord("a")
                charts[char_num] += 1
            result[tuple(charts)].append(string)
        return list(result.values())