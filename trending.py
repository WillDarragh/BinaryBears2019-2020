# trending

tweets = {}

for n in range(int(input())):
    words = input().split()
    for w in words:
        if w[0] == '#':
            tag = w[1:].lower().strip().strip('.').strip('!').strip('?')
            if tag not in tweets:
                tweets[tag] = 1
            else:
                tweets[tag] += 1

arr = []

for key,val in tweets.items():
    arr.append((key,val))

arr = sorted(arr,key=lambda x: x[0])
arr = sorted(arr,key=lambda x: x[1],reverse=True)

for a in arr:
    print(a[1],a[0])
