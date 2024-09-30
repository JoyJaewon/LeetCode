from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for s in word:
                count[ord(s) - ord('a')] += 1
            ans[tuple(count)].append(word)
        
        return ans.values()
        