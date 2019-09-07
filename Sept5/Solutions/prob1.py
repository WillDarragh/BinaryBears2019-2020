# Prob 1 Elo

T = int(input())

scores = []

for t in range(T):
	name, wl, ranks = input().split(maxsplit=2)
	w,l = map(int, wl.split('-'))
	ranks = list(map(int, ranks.split()))

	score = (sum(ranks)+400*(w-l))/len(ranks)

	scores.append((name,score))

scores.sort(key=lambda x: x[1],reverse=True)

for t in range(T):
	print(f'{t+1}){scores[t][0]} {round(scores[t][1],2):.2f}')
