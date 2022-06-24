class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        # 정규식으로 불필요한 문자 필터링->문자열 전체에서 한 번에 영숫자만 걸러내도록 함
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1] # 슬라이싱