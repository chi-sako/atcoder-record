# 3つのマス目に0か1が書かれている。1が書いてあるマス目の数を表示する。
# 入力例：001

nums = input()
count = 0
for num in nums:
  count += int(num)
print(count)
  