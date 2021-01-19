contador = int(input("Contagem regressiva começando em: "))
separador = str(input("O que deseja usar para separar os números? "))
print('Iniciando contagem regressiva de {} a 0...'.format(contador))
while contador >= 0:
    if contador != 0:
        print(contador, end=' '+separador+' ')
    else:
        print(contador, end='\n')
    contador -= 1

print('Cabou mermão!!!')
