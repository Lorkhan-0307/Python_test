import sys
read = sys.stdin.readline().rstrip

N, M, K = map(int,read().split()) # N_배열의 크기/M_숫자 더해지는 횟수/K_연속 합
Nums = list(map(int,input().split())) # 수 읽기

Sum = 0 # 배열의 합

Nums.sort() # 작은 수 부터 정렬

if(Nums[N-1]==Nums[N-2]):
  Sum = Nums[N-1]*M
else:
  Rest = M%(K+1)
  portion = M//(K+1)
  Sum = Nums[N-1]*K*portion + Nums[N-2]*portion #K개씩 띄우면서 더하기
  Sum += Nums[N-1]*Rest

print(Sum)
