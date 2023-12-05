# 卵 6個入りのパックは S円、卵 8個入りのパックは M円、卵 12個入りのパックは L円
# どのパックも何パックでも購入できるとき、N個以上の卵を買うために必要な最小の金額は？
# 1 <= N <= 100, 1 <= S,M,L <= 10^4

N, S, M, L = map(int, input().split())

ans = 10**8
for x in range(20):
  for y in range(15):
    for z in range(10):
      if((6*x + 8*y + 12*z) >= N):
        ans = min(ans, S*x+M*y+L*z)
        
print(ans)

  
