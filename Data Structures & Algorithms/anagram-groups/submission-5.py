class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''

        store each words counter with array in a hmap as key 
        and words as values & compare and add. Then convert all
        values to list

        '''

        hmap = {}

        for s in strs:

            freq = [0] * 26

            for c in s:
                index = ord(c) - ord('a')
                freq[index] += 1

            key = tuple(freq)
            
            if key not in hmap:
                hmap[key] = [s]
            else:
                hmap[key].append(s)
        
        return list(hmap.values())
