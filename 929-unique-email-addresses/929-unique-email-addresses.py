class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        alf = set()
        for email in emails:
            word = []
            i = 0
            domain = False
            while i < len(email):
                if email[i] == "+" and not domain:
                    while email[i] != "@":
                        i += 1
                
                elif email[i] == "." and not domain:
                    i += 1
                else:
                    if email[i] == "@":
                        domain = True
                    word.append(email[i])
                    i += 1
            alf.add("".join(word))
        return len(alf)