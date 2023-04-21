class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        persons = [defaultdict(int) for _ in range(n + 1)]
        persons[0][0] += 1
        for i in range(len(group)):
            now = [defaultdict(int) for _ in range(n + 1)]
            for j, person in enumerate(persons):
                for value, count in person.items():
                    now[j][value] += count
                if j + group[i] > n:
                    continue
                # print(persons[0])
                for value, count in person.items():
                    # print(j, value, count)
                    if value == float("inf") or value + profit[i] >= minProfit:
                        now[j + group[i]][float("inf")] += count
                    else:
                        now[j + group[i]][value + profit[i]] += count
            if now[0][0] == 0:
                now[0][0] = 1
            persons = now
            # print(now)
        ans = 0
        for i, person in enumerate(persons):
            if i == 0:
                continue
            ans += person[float("inf")]
        if minProfit == 0:
            ans += 1
        return ans %( 10**9 + 7)
                
            