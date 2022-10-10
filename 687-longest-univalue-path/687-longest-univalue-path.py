class Solution:
    result: int=0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            
            # 왼쪽 오른쪽으로 노드가 존재하지 않을 때까지 DFS 재귀 
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 현재 노드가 자식 노드와 동일한 경우 거리 l 추가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            
            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값
            self.result = max(self.result , left + right)
            # 자식 노드 값 중에서 큰 값 확인
            return max(left , right)
        
        dfs(root)
        return self.result 