class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        else:
            st={}
            tt = {}
            for i in s:
                if i in st:
                    st[i]+=1
                else:
                    st[i]=1
            for i in t:
                if i in tt:
                    tt[i]+=1
                else:
                    tt[i]=1
        if st==tt:
            return True
        else:
            return False           