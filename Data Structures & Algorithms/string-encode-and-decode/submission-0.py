class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Find the separator '#'
            j = i
            while s[j] != "#":
                j += 1

            # Length of the next string
            length = int(s[i:j])

            # Move i to the start of the string
            i = j + 1

            # Extract the string
            res.append(s[i:i + length])

            # Move i to the next encoded string
            i = i + length

        return res