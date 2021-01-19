valor_inicial = 0
quebra_linha = 0
passo = 1000
for num in range(valor_inicial, 100_000+passo, passo):
    if quebra_linha <= 5:
        if quebra_linha == 0:
            print('[ ', end=' ')
        print(num, end=' ')
        quebra_linha += 1
    else:
        print(' ]', end='\n')
        quebra_linha = 0
