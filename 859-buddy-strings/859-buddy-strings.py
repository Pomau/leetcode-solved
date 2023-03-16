class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        count = 0
        alf = defaultdict(int)
        is_replay = False
        for i, ch in enumerate(s):
            if ch != goal[i]:
                count += 1
            if ch in alf:
                is_replay = True
            alf[ch] += 1
            alf[goal[i]] -= 1
        for key, item in alf.items():
            if item != 0:
                return False
        return count == 2 or count == 0 and is_replay