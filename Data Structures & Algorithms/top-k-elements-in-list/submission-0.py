class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create a hashmap, where the key will be the number, value will be frequency
        freq_map = Counter(nums)
        # create a list of tuples, (num, freq)
        tuple_list = []
        for x, v in freq_map.items():
            tuple_list.append((x, v))
        # sort list by freq, inverse
        tuple_list.sort(key = lambda x: x[1])

        # pop k elements, and only use the num
        res = []
        for _ in range(k):
            res.append(tuple_list.pop()[0])
        return res

