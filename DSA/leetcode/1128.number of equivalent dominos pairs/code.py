
class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        hm = {}
        for each in dominoes:
            if each[0] < each[1]:
                s, e = each[0], each[1]
            else:
                s, e = each[1], each[0]
            
            if f"{s}_{e}" in hm:
                hm[f"{s}_{e}"] += 1
            else:
                hm[f"{s}_{e}"] = 1
        
        return sum([ (i * (i-1)//2) for i in hm.values() if i!= 1])