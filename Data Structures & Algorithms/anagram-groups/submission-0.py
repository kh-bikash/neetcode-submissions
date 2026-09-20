class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #We place similar character words into group but order can be different
        #We can sort it then see if they are similar
        res=defaultdict(list)#Mapping character count
        for s in strs:
            count=[0]*26#a-z
            for c in s:
                count[ord(c)-ord("a")]+=1
            res[tuple(count)].append(s)
        return list(res.values())