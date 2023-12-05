# 1年が 1月から M月までの Mヵ月で、どの月も1ヵ月が 1日から D日までの D日間であるとき
# y年m月d日の翌日は何年何月何日か？

M, D = map(int, input().split())
y, m, d = map(int, input().split())

if(m*d == M*D):
  print(y+1, 1, 1)
elif(d == D):
  print(y, m+1, 1)
else:
  print(y, m, d+1)