class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[''.join(sorted(list(s)))].append(s)
        answer = []
        for key in groups.keys():
            answer.append(groups[key])
        return answer
        