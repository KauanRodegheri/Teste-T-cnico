string = str(input('digite sua string: '))
count=0
if 'a' in string or 'A' in string:
    for i in string:
        if i in 'aA':
            count+=1
    print(f'letra A encontrada {count}')
else:
    print('Letra A não foi encontrada')