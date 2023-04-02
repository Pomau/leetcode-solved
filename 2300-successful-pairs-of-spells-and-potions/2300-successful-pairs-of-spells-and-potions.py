class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = [0 for i in range(len(spells))]
        spells = [[spells[i], i] for i in range(len(spells))]
        spells.sort()
        potions.sort(reverse=True)
        l_spells = 0
        l_potions = -1
        while l_spells < len(spells):
            while l_potions + 1 < len(potions) and potions[l_potions + 1] * spells[l_spells][0] >= success:
                l_potions += 1
            ans[spells[l_spells][1]] = l_potions + 1
            l_spells += 1
        return ans