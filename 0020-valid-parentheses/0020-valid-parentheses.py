class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "}": "{", "]": "["}
        stk=[]

        for si in s:
            if si not in hashmap:
                stk.append(si)
            else:
                if not stk:
                    return False
                else:
                    popp=stk.pop()
                    if popp != hashmap[si]:
                        return False
        return not stk


        