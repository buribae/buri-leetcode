from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #         res = collections.defaultdict(list)

        #         for s in strs:
        #             res[tuple(sorted(s))].append(s)

        #         return res.values()

        res = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()
