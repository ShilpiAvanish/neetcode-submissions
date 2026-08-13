class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # store each mapping in a map as a key, and add anagrams to the value list
        # convert all the values to a list at the end

        letter_count_dict = defaultdict(list)

        for word in strs:

            mapping = [0] * 26
            for c in word:
                mapping[ord(c) - ord("a")] += 1

            letter_count_dict[tuple(mapping)].append(word)

        return list(letter_count_dict.values())