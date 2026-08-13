class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in strs:
            letterCounter = [0] * 26
            for letter in string:
                indexLocation = ord(letter) - ord("a")
                letterCounter[indexLocation] += 1
            ans[tuple(letterCounter)].append(string)
        return ans.values()
            
