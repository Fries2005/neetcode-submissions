class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + '#' + string
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        index = 0
        decoded = []
        while index < len(s):
            count = ""
            while s[index] != '#':
                count += s[index]
                index += 1

            curr = ""
            for _ in range(int(count)):
                index += 1
                curr += s[index]
            decoded.append(curr)
            index += 1

        return decoded

    
