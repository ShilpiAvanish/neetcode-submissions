class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = {}

        for string in strs:
            char_freq = [0] * 26
            for c in string:
                index = ord(c) - ord('a')
                char_freq[index] += 1

            key = tuple(char_freq)
            if key in hashset:
                hashset[key].append(string)
            else:
                hashset[key] = [string]

        return list(hashset.values())
