contador = 1

print('WHILE')
print('[', end=' ')
while contador <= 100:
    print(contador, end=', ')
    contador += 1
print(']', end='\n')

print('\n')

print('FOR')
print('[', end=', ')
for num in range(1, (100+1)):
    print(num, end=' ')
print(']', end='\n')
