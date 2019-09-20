# royal tweet

count = 0

N = int(input())

for n in range(N):
    line = input().lower()

    if '@BritishMonarchy'.lower() in line:
        count += 1

print(f'Total Tweets Containing @BritishMonarchy = {count}')
