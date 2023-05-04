class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = senate.count("R")
        s = senate.count("D")
        r_kill = s_kill = 0
        live = [True] * len(senate)
        while r != 0 and s != 0:
            # print(r, s, r_kill, s_kill, live)
            for i in range(len(senate)):
                if not live[i]:
                    continue
                if r_kill > 0 and senate[i] == "R":
                    r_kill -= 1
                    r -= 1
                    live[i] = False
                elif s_kill > 0 and senate[i] == "D":
                    s_kill -= 1
                    s -= 1
                    live[i] = False
                else:
                    if senate[i] == "D":
                        r_kill += 1
                    else:
                        s_kill += 1
        if r == 0:
            return "Dire"
        else:
            return "Radiant"
            