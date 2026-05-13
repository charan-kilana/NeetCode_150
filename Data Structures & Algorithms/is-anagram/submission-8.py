class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # BFM
        # dict_s={}
        # dict_t={}

        # for i in s:
        #     if i in dict_s:
        #         dict_s[i]=dict_s[i]+1
        #     else:
        #         dict_s[i]=1
        
        # for j in t:
        #     if j in dict_t:
        #         dict_t[j]=dict_t[j]+1
        #     else:
        #         dict_t[j]=1
        
        # res_s = dict(sorted(dict_s.items()))
        # res_t = dict(sorted(dict_t.items()))

        # if res_s == res_t:
        #     return True
        # else:
        #     return False

        # easiest method using sorted
        if sorted(s) == sorted(t):
            return True
        else: 
            return False
        