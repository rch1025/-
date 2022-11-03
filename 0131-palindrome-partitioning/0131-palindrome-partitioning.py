class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def go(s, part):
            if not s:
                answer.append(part)
                
            for i in range(len(s)):
                if checkPalindrome(s[:i+1]):
                    go(s[i+1:], part+[s[:i+1]])
                    
        def checkPalindrome(s):
            return s == s[::-1]
        
        answer = []
        go(s, [])
        return answer 
    