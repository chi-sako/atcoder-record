# 正整数 Dに対して |x^2 + y^2 - D|の最小値を求めよ
# ただし、x,yは非負整数

import math

def calc_f(x, y):
  return abs(x*x + y*y -D)

D = int(input())
lim_x = math.ceil(math.sqrt(D))

for x in range(lim_x):
  c = x*x-D
  if(c >= 0):
    y = 0
  else:
    y1 = math.ceil(math.sqrt(-c))
    y2 = math.floor(math.sqrt(-c))
    if(calc_f(x,y1) <= calc_f(x,y2)):
      y = y1
    else:
      y = y2
  
  if(x==0):
    num_min = calc_f(x,y)
  else:
    if(calc_f(x,y) < num_min):
      num_min = calc_f(x,y)

print(num_min)