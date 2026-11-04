class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False
        
        freq1 = {}
        freq2 = {}
        for i in range(len1):
            if s1[i] not in freq1:
                freq1[s1[i]] = 1
            else:
                freq1[s1[i]] += 1

            if s2[i] not in freq2:
                freq2[s2[i]] = 1
            else:
                freq2[s2[i]] += 1
         
        if freq1 == freq2:
            return True

        for i in range(len1, len2):
            if freq2[s2[i - len1]] <= 1:
                del freq2[s2[i - len1]]
            else:
                freq2[s2[i - len1]] -= 1
            
            if s2[i] not in freq2:
                freq2[s2[i]] = 1
            else:
                freq2[s2[i]] += 1

            if freq2 == freq1:
                return True
        
        return False