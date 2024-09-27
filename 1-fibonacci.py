int = int(input('digite seu numero: '))

lista = [0, 1]
while lista[-1] <= int:
    if int == lista[-1] + lista[-2]:
        lista.append(lista[-1] + lista[-2])
    else:
        lista.append(lista[-1] + lista[-2])


print(lista)
if int in lista:
    print('seu numero faz parte do fibonacci')
else:
    print('seu numero não faz parte do fibonacci')