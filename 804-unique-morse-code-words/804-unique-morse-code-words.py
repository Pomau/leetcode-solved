class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alf = [ ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."
              ]
        different = set()
        for word in words:
            now = []
            for ch in word:
                now.append(alf[ord(ch) - ord("a")])
            different.add("".join(now))
        return len(different)