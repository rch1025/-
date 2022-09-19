class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS 함수 설정
        def dfs(i,j):
            # 인덱스가 범위 밖으로 나가거나 1이 아닌 경우 반환 설정
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != "1":
                return
            # 1을 0으로 전환
            grid[i][j] = "0"

            # 동서남북
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 뿌리 노드 
                if grid[i][j] == "1":
                    # 인접한 1에 대하 count 설정
                    dfs(i,j)
                    count += 1
        return count