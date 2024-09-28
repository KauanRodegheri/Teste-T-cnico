string = str(input('digite sua string: '))
#1° forma
count=0
if 'a' in string or 'A' in string:
    for i in string:
        if i in 'aA':
            count+=1
    print(f'letra A encontrada {count} vezes')
else:
    print('Letra A não foi encontrada')

#2° forma
count=0
for letra in string:
    if letra in 'Aa':
        count+=1
if count >=1:
    print(f'foram encontrados {count} letra A')
else:
    print('não tem A')

#3° forma
lista = []
for letra in string:
    if letra in 'Aa':
        lista.append(letra)

if lista:
    print(f'foram encontrados {len(lista)} letra A')
else:
    print('não tem A')