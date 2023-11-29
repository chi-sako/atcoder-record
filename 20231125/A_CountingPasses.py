# N人の人がある試験を受けた。L点以上で合格。合格した人数は？

N, L = map(int, input().split())
scores = list(map(int, input().split()))
passes = [score for score in scores if score >= L]
print(len(passes))