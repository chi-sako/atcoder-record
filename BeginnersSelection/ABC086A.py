# 2つの整数a,bの積が偶数か奇数か判定する。
# 1 <= a,b <= 10000

a,b = map(int,input().split())
if(a*b % 2 == 0):
  print('Even')
else:
  print('Odd')