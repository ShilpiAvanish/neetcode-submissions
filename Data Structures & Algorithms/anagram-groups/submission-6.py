class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # store each mapping in a map as a key, and add anagrams to the value list
        # convert all the values to a list at the end

        letter_count_dict = {}

        for word in strs:

            mapping = [0] * 26
            for c in word:
                mapping[ord(c) - ord("a")] += 1

            tuple_mapping = tuple(mapping)

            if tuple_mapping in letter_count_dict:
                letter_count_dict[tuple_mapping].append(word)
            else:
                letter_count_dict[tuple_mapping] = [word]
                
        return list(letter_count_dict.values())