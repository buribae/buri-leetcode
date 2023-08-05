from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # 1
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

        """
        #2
        freq = collections.defaultdict(int)

        for n in nums:
          freq[n] += 1
        
        return sorted(freq, key=freq.get, reverse=True)[:k]
        """
