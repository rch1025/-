class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []
        map_table = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for word in s:
            # dict에서의 in은 key에 들어있는지만 봄
            if word not in map_table:
                stack_list.append(word)
            # 대칭 모양이 같으면 elif문 통과 안 함
            elif not stack_list:
                return False
            elif map_table[word] == stack_list.pop():
                pass
            else:
                return False
        if len(stack_list)>0:
            return False
        else:
            return True