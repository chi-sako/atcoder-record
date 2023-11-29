# 長さNの整数列 A=(A1, A2,...,AN)及び整数 L<=R
# i=1,2,...,N について以下の2条件を満たす Xiを求めよ
# 条件1：L <= Xi <= R
# 条件2：L <= Y <= R を満たすどの整数Yについても |Xi-Ai| <= |Y-Ai|


N, L, R = map(int, input().split())
A = list(map(int, input().split()))
X = []
for i in range(N):
  if(A[i] <= L):
    X.append(L)
  elif(A[i] >= R):
    X.append(R)
  else:
    X.append(A[i])
X = [str(x) for x in X]
X = " ".join(X)
print(X)