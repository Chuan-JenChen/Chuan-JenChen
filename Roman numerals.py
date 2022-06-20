class solution:
    def romanNumber(self,s:str):
        map={'I':1,'V':5,'x':10,'L':50,'C':100,'D':500,'M':1000}
        Number=0
        for i in range[len(s)-1]:
            if map[s[i]]>map[s[i+1]]:
                Number=Number + map[s[i]]
            else map[s[i]]<map[s[i+1]]:
                 Number=Number - map[s[i]]
        Number=Number+map[s[i]]
        return Number



