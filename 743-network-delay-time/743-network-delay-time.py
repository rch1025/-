class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        gg = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            gg[u].append((v, w))
            
        # 큐
        Q = [(0, k)]
        dist = collections.defaultdict(int)
        
        # 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in gg[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
                    
        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1