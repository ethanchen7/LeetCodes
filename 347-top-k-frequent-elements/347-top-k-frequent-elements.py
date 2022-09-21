class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # get the frequencies of each number
        # store the frequencies as arrays of arrays and their frequencies are the index
        # index the frequencies from the end for k amount
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for num, c in count.items():
            freq[c].append(num)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result