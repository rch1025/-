class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """jewel의 개별 글자가 들어가 있기만 하면 됨"""
        stones_dict = {}
        for word in stones:
            if word not in stones_dict.keys():
                stones_dict[word]=1
            else:
                stones_dict[word]+=1
        c = 0
        for j_word in jewels:
            if j_word in stones_dict.keys() :
                c += stones_dict[j_word]
            else:
                pass
        return c