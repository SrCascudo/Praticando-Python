multiplo = int(input("Informe um número que deseja ver seus múltiplos: "))
repeticao = int(input("Quantos múltiplos de {} deseja ver? ".format(multiplo)))

print('---------WHILE---------')
index = 1
while index <= repeticao:
    print(multiplo * index, end='; ')
    index += 1
print('\n-----------------------')

print('----------FOR----------')
for obj in range(1, repeticao+1):
    print(obj*multiplo, end='; ')
print('\n-----------------------')
