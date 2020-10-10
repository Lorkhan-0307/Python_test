import sys
read = sys.stdin.readline().rstrip

N, M = map(int, read().split()) # N x M
Card = [[0]*M for _ in range(N)] # 2차원 리스트
Num = [0]*N

for i in range(N):
  Card[i] = list(map(int, input().split()))

for i in range(N):
  Num[i] = min(Card[i]) # 각 행의 최솟값

print(max(Num)) # 최솟값들의 최댓값 출력
