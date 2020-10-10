import sys
read = sys.stdin.readline().rstrip

''' 500, 100, 50, 10원으로 거슬러 줌, but 거슬러 주는 동전의 최소 개수를 구하라'''

def give(N, coin):
  i = N // coin
  return i

Cash = int(read()) #돈 읽기
List_coin = (500, 100, 50, 10) # 동전 튜플 생성
change = [0]*len(List_coin)

for i in range(len(List_coin)):
  change[i] = give(Cash, List_coin[i])
  Cash -= List_coin[i]*change[i]

print(sum(change))
