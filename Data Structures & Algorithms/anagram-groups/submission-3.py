class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #if no value it will auto set to an array
        result  = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for letter in word:
                key[ord(letter) - ord('a')] += 1

            #change the list which is mutable to a immutable tuple
            result[tuple(key)].append(word)
        
        return list(result.values())
