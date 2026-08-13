class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):
            # Find the delimiter '#'
            j = i
            while s[j] != "#":
                j += 1
            num_letters = int(s[i:j])  # Extract the length of the word
            word = s[j + 1: j + 1 + num_letters]  # Extract the word
            result.append(word)
            i = j + 1 + num_letters  # Move index to the next encoded word
        
        return result
