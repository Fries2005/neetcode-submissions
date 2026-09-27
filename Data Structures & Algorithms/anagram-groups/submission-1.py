from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)
        result = []

        # logic here
        for string in strs:
            counts = [0] * 26
            for char in string:
                counts[ord(char) - ord('a')] += 1

            freq_map[tuple(counts)].append(string)

        for _, lst in freq_map.items():
            result.append(lst)

        return result
