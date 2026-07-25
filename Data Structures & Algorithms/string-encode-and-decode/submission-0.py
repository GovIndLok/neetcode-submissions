class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += f"#{len(string)} {string}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 1
        while i < len(s):
            j = i
            while s[j] != " ":
                j += 1
            lenth_str = int(s[i:j])
            strings.append(s[j+1:j+1+lenth_str])
            i = j + 2 + lenth_str
        return strings