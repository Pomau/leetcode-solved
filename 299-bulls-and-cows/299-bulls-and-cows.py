class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        alf = defaultdict(int)
        bull = 0
        cow = 0
        for i, el in enumerate(secret):
            if el != guess[i]:
                alf[el] += 1
        for i, el, in enumerate(guess):
            if el == secret[i]:
                bull += 1
            elif alf[el] > 0:
                alf[el] -= 1
                cow += 1
        return f"{bull}A{cow}B"
        