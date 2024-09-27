print('''
A)1, 3, 5, 7, \033[31m9 #o elemento será a soma do ultimo + 2\033[m 
B)2, 4, 8, 16, 32, 64, \033[31m128 # o elemento será a multiplicação por 2\033[m
C)0, 1, 4, 9, 16, 25, 36, \033[31m49 # o elemento será o quadrado dos numeros inteiros \033[m
D)4, 16, 36, 64, \033[31m100 # o elemento será o quadrado nos numeros pares\033[m
E)1, 1, 2, 3, 5, 8, \033[31m13 #sequencia de fibonacci\033[m
F)2, 10, 12, 16, 17, 18, 19, \033[31m200 #o elemento será o proxima a começar com a letra D\033[m
''')

lista = {
    'a': [1, 3, 5, 7],
    'b': [2, 4, 8, 16, 32, 64],
    'c': [0, 1, 4, 9, 16, 25, 36],
    'd': [4, 16, 36, 64],
    'e': [1, 1, 2, 3, 5, 8],
    'f': [2, 10, 12, 16, 17, 18, 19]
    }

for k,v in lista.items():
    if k == 'a':
        v.append(v[-1] + 2)
    elif k == 'b':
        v.append(v[-1] * 2)
    elif k == 'c':
        v.append(v[-1] + 13)
    elif k == 'd':
        v.append(10 ** 2)
    elif k == 'e':
        v.append(v[-1] + v[-2])
    elif k == 'f':
        v.append(200)

    print(f'{k}: {v}')
