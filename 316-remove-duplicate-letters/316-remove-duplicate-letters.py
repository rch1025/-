class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s)
        seen_set = set()
        ll = []

        for char in s :
            counter[char] -= 1
            if char in seen_set:
                continue
            while ll and char < ll[-1] and counter[ll[-1]] > 0: # 마지막 스택 제거
                seen_set.remove(ll.pop( ))
            ll.append(char)
            seen_set.add(char)
        return ''.join(ll) 
