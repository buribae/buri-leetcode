from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        freq_list = [0] * 26
        map = { freq_list: [] }
        return map.values
        """

        ans = collections.defaultdict(list)
        for s in strs:
            freqs = [0] * 26
            for c in s:
                freqs[ord(c) - ord("a")] += 1
            ans[tuple(freqs)] += [s]

        return ans.values()
