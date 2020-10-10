import sys
read = sys.stdin.readline().rstrip

N, K = map(int, read().split()) # N, 나누는 수 K
i = 0 # 횟수

while True:

  if N%K == 0: # 나누어 떨어지는 경우
    N=N/K
    i+=1

  else: #나누어 떨어지지 않아서 1을 빼야할 경우
    T = N%K
    if T==N: # N보다 K가 더 클 경우
      i+=N-1
      break
    N = N-(N%K) 
    i += T # 뺀 횟수많큼 실행 횟수 더하기

  if N==1: # 1이 되면 종료
    break

print(i)
