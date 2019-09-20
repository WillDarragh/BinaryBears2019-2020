# xedni

words = []

N = int(input())

for n in range(N):
    words.append(input()[::-1])

for w in sorted(words,key=lambda a: a[0]):
    print(w)

