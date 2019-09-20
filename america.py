# codeforamerica

city = input()
while(city!='End'):

    line = input().lower()

    message = ''

    if 'lead' in line and 'flexib' in line and 'involve' in line and 'plan' in line:
        message = 'Meets standards'
    else:
        message = 'Does not meet standards'




    print(f'{city}: {message}')
    city = input()
