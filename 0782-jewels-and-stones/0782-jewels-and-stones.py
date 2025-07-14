class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        sett=set(jewels)

        for stone in stones:
            if stone in sett:
                count+=1
            
        return count



         
        